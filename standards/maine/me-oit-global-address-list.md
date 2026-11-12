---
schema_version: 1
corpus: states-government-it
jurisdiction: maine
id: me-oit-global-address-list
title: Global Address List Standard
doc_type: standard
citation: MaineIT Global Address List Standard
authority_level: ''
issuing_body: Maine Office of Information Technology (MaineIT), Department of Administrative and Financial
  Services
source_url: https://www.maine.gov/oit/sites/maine.gov.oit/files/inline-files/GALStandard.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 87f6283f4bccf6cb8366b7d83e6ae90a2399c6b004cfef57e29387aceec13c33
effective_date: null
source_version: 'Latest Revision Date: August 21, 2026'
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

# Global Address List Standard (MaineIT Global Address List Standard)

## At a glance

The standard by which OIT manages the Global Address List of the State's Enterprise Messaging System, so that mailbox address and contact information is managed by approved methods.

## Full text

                                  Maine State Government
                        Dept. of Administrative & Financial Services
                          Office of Information Technology (OIT)

                  Email Global Address List Management Standard
1.0.   Purpose
1.1.   Through this Standard, the Office of Information Technology (OIT) manages the
       State’s Enterprise Messaging System’s Global Address List (GAL, see Definitions).
       The purpose of this Standard is to ensure that approved methods and procedures
       are followed in managing mailbox address/contact information and Global
       Distribution Lists (GDLs, see Definitions).

1.2.   Additionally, OIT must comply with the Freedom of Access Act 1 (FOAA), and Public
       Law Chapter 583- An Act to Amend the Notice of Risk to Personal Data Act. 2

2.0.   Definitions
2.1.   Active Directory (AD) User Account: For this Standard, this refers to user identifiers
       contained within AD which have email addresses attached. This excludes AD
       accounts such as service and administrator, which do not have associated email
       addresses.

2.2.   Email Address: For this Standard, this includes individuals’ user accounts
       (firstname.lastname@maine.gov), and Resource Accounts used to identify
       conference rooms, aliases on web pages (for example, webmaster@maine.gov),
       shared-access calendars, etc.

2.3.   Computing Infrastructure and Services Leadership: The OIT Director or OIT Deputy
       Director who are among the leadership staff within the OIT Computing
       Infrastructure and Services team.

2.4.   Global Address List (GAL): The GAL is a Microsoft Exchange directory service, which
       contains information for all email users, distribution groups, and Exchange
       resources.

2.5.   Global Distribution List (GDL): A GDL is a list of @maine.gov user accounts, created
       by OIT, which may be viewed and used by all users of the State’s Enterprise
       Messaging System.

2.6.   Personal Distribution List (PDL): A PDL lists any number of user accounts, including
       email address from outside State government, created by individual Enterprise

   1 http://legislature.maine.gov/legis/statutes/1/title1sec408-A.html
   2 https://legislature.maine.gov/statutes/10/title10ch210-B.pdf

                                                 Page 1 of 5

       Messaging System users. Only the personal distribution list owner can create,
       manage, and use them.

2.7.   Resource Accounts: Mailboxes used for conference rooms, aliases on web pages, and
       shared calendars, not a person.

3.0.   Applicability
3.1.   This Standard is intended to manage the requests for:
       3.1.1. Creating and managing State email addresses (see Definitions);
       3.1.2. Creating and managing GDLs;
       3.1.3. Managing access to public information contained in the GAL properties; and
       3.1.4. Managing AD user account name exception requests.

3.2.   This Standard is intended to manage requests by:
       3.2.1. Executive Branch and semi-autonomous State agencies;
       3.2.2. Agencies from other Maine State government branches that use Executive
              Branch managed services; and
       3.2.3. Vendors approved by the OIT Computing Infrastructure and Services
              Leadership (see Definitions).

4.0.   Responsibilities
4.1.   The OIT Computing Infrastructure and Services Leadership is responsible for
       enforcement of these standards and manages the process for approving the creation
       and management of all messaging accounts.

4.2.   OIT’s Enterprise Messaging System staff are responsible for applying the standards
       and procedures for global address list management.

4.3.   OIT Account Managers approve all requests for the creation of GDLs and Resource
       Accounts (see Definitions) and will communicate any special needs to the OIT
       Computing Infrastructure and Services Leadership.

4.4.   Authorized individuals within the Bureau of Human Resources (BHR) certify AD
       user account name requests that are exceptions to the characteristics described in
       5.1.2. An authorized individual is anyone at the BHR Director level or above.

4.5.   Governmental entities using the State’s wide area network, but not participating in
       the Enterprise Messaging System may be granted real-time access to the GAL by the
       OIT Computing Infrastructure and Services Leadership.

4.6.   Enterprise Messaging System users may create Personal Distribution Lists (PDLs,
       see Definitions) from the Contacts section of Outlook. PDLs may contain non-state
       email addresses and are maintained and deleted by their creators.

                                          Page 2 of 5

5.0.     Directives
5.1.     Global Address List – The GAL is established by the OIT Enterprise Messaging
         System staff to provide contact and email information to users and has the following
         characteristics.
         5.1.1. Resource Accounts, which are accounts that are not real user’s names, i.e.
                mailboxes used for conference rooms, aliases on web pages, and shared
                calendars must use a firstname.lastname naming convention. Resource
                Account examples are as follows:
                5.1.1.1. Conference rooms must have a last name that references the
                          department and/or building that it is set up for:
                          ConfRm1.MaineDOT.
                5.1.1.2. Aliases for webmasters must have a last name that references the
                          department it is set up for: Webmaster.MaineDOT.
                5.1.1.3. Mailboxes used as shared calendars must have a last name that
                          references the department it is set up for: Region1.MaineDOT.
                5.1.1.4. Resource Accounts that pre-date this Standard, and use an
                          alternative naming convention, are grandfathered, provided the
                          name can be related to the associated agency. Legacy naming
                          conventions that pre-date this Standard may not be used for net-
                          new users or assets.

         5.1.2. New Active Directory (AD) user accounts are created automatically based on
                employee records from the State’s Human Resources system (PRISM)
                through the Bureau of Human Resources. To ensure consistency and prevent
                naming confusion, account names shall be generated in the following order of
                precedence. OIT will use the first available option:
                5.1.2.1. Legal name without middle initial.
                5.1.2.2. Legal name with middle initial.
                5.1.2.3. Preferred name without middle initial.
                5.1.2.4. Preferred name with middle initial.

         5.1.3. The AD alias (the name displayed in the Global Address List [GAL]) must
                remain consistent with the AD account name (See Identification and
                Authentication Policy and Procedures 3, section 8.4.1.). The use of nicknames
                in the account name is prohibited. However, a nickname may appear as an
                alias in parentheses following the real name.
                5.1.3.1. Example: Nickname: Scotty AD Name: Maxamillian.Scott.Desjardins
                          GAL Alias: Desjardins, Maxamillian S (Scotty)

         5.1.4. Changes or exceptions to the AD account name described in 5.1.2. must
                receive certification from an authorized individual within BHR. For
                exceptions, the certification is documented in AD to capture the certifier and
                the date the certification was received by OIT to maintain a chain of custody.

   3
       https://stateofmaine.sharepoint.com/sites/MaineIT/SitePages/Policies.aspx

                                                    Page 3 of 5

              The AD account name and GAL alias are then changed to the certified
              exception from BHR.

       5.1.5. For other-party mail-relay services established in accordance with Section
              6.5.6 of the Domain Name Policy & Procedure 4, the format of the fully
              qualified email is either <Program>.<Agency>@mail-#.maine.gov or
              <Program>-<Agency>@mail-#.maine.gov.

5.2.   Global Distribution Lists are established by OIT’s Enterprise Messaging System staff
       upon
       5.2.1. Approval by the OIT Account Manager and
       5.2.2. Receipt of a work order generated by the Customer Support Center (CSC).

5.3.   The GDL’s names will be assigned in compliance with the following conventions and
       examples and will appear in bold face in the GAL as established by the OIT
       Computing Infrastructure and Services Leadership.
       5.3.1. Examples:
              5.3.1.1. DHHS-221 State
              5.3.1.2. ATT_Criminal_Div (ATT is the three-character Attorney General’s
                       Office identifier)
              5.3.1.3. Audit

       5.3.2. Conventions:
              5.3.2.1. GDLs will only contain contact information for
                       firstname.lastname@maine.gov accounts (no non-state email
                       addresses will be included).
              5.3.2.2. A role-based owner must be assigned to maintain the GDL at the
                       time of creation.
              5.3.2.3. Descriptions of the use of the GDL, creation date, and requestor’s
                       name must be documented in the Notes field of the list’s AD entry.

5.4.   The OIT Computing Infrastructure and Services Leadership will:
       5.4.1. Work with the CSC to develop forms to collect the needed information to
              manage the Enterprise Messaging System.

       5.4.2. Oversee GAL, GDL, and Resource Account creation to ensure compliance with
              this Standard.

       5.4.3. Annually, or upon request, provide lists of current GDLs to OIT Account
              Managers for their review to ensure the GDLs are still active.

       5.4.4. Bring issues relative to the efficient management of the messaging system to
              the attention of the Core Technologies management for resolution.

   4 https://www.maine.gov/oit/sites/maine.gov.oit/files/inline-files/DomainNamePolicyProcedure.pdf

                                              Page 4 of 5

       5.4.5. Provide rates and fees associated with this Standard for publication.

6.0.   Document Information
6.1.   Initial Issue Date: August 31, 2007
6.2.   Latest Revision Date: August 21, 2026
6.3.   Point of Contact: PolicyTeam.OIT@Maine.Gov
6.4.   Approved By: Chief Information Officer, OIT
6.5.   Legal Citation: Title 5, Chapter 163: Office of Information Technology 5
6.6.   Waiver: Waiver Policy 6
6.7.   FOAA: FOAA Policy 7
6.8.   Distribution: Internet 8

   5 https://legislature.maine.gov/statutes/5/title5ch163sec0.html
   6 https://www.maine.gov/oit/sites/maine.gov.oit/files/inline-files/waiver.pdf
   7 https://www.maine.gov/oit/sites/maine.gov.oit/files/inline-files/FOAAPolicy.pdf
   8 https://www.maine.gov/oit/policies-standards

                                                Page 5 of 5

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
