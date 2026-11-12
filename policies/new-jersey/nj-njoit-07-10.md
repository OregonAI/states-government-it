---
schema_version: 1
corpus: states-government-it
jurisdiction: new-jersey
id: nj-njoit-07-10
title: Use of Statewide Disaster Recovery Facilities Policy
doc_type: policy
citation: NJOIT Technology Circular 07-10-NJOIT
authority_level: ''
issuing_body: New Jersey Office of Information Technology
source_url: https://www.nj.gov/it/docs/ps/07-10_NJOIT_Use_of_Statewide_Disaster_Recovery_Facilities.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 4de0ef9d4f1506b5f054c3494a98eae9762ce37ef50f79b8825d52ba84dc8354
effective_date: '2007-06-11'
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
- cloud-resilience
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Use of Statewide Disaster Recovery Facilities Policy (NJOIT Technology Circular 07-10-NJOIT)

## At a glance

Requirements for placing equipment and application environments at the State's disaster recovery facilities for mission-critical business functions.

## Full text

     
                  NJ OFFICE OF INFORMATION TECHNOLOGY               P.O. Box 212               www.tech.nj.gov
                  Philip D. Murphy, Governor                        300 Riverview Plaza
                  Christopher J. Rein, Chief Technology Officer       Trenton, NJ 08625-0212

                                                                POLICY NO:
              STATE OF NEW JERSEY                                                07-10-NJOIT
             TECHNOLOGY CIRCULAR                                SUPERSEDES:              EFFECTIVE DATE:
                                                                           NA                06-11-2007
          Use of Statewide Disaster                             VERSION:                 LAST REVIEWED:
          Recovery Facilities Policy                                       3.0               12-13-2024

1.       PURPOSE
         This policy defines specific requirements for placing equipment and/or application environments
         at the New Jersey’s disaster recovery facilities in support of mission- critical business functions.

         It establishes a directive for the use of disaster recovery facilities; and

         Provides direction regarding the requirements for establishing disaster-recovery capability at
         disaster recovery facilities.

2.       SCOPE
         This policy applies to all State Departments, Agencies, “in but not of” entities, their employees,
         contractors, consultants, temporary workers, and others who are responsible for building and/or
         developing information technology environments that support disaster recovery for critical
         business functions as defined in Business Impact Analysis (BIA) reports.

3.       DEFINITIONS
         Please refer to the Statewide Policy Glossary at http://www.nj.gov/it/ps/glossary/.

4.       POLICY
         4.1. Agency participation and access to the disaster recovery facility:
                4.1.1.     Applications and hardware platforms must support mission-critical functions,
                           as defined in the agency's Continuity of Operations (COOP) plan and/or BIA;

                4.1.2.     Applications and hardware platforms must be compatible with currently

07-10-NJOIT, Use of Statewide Disaster Recovery Facilities Policy                                          Page 1 of 4

                           installed and supported infrastructure within the disaster recovery facility; and

                4.1.3.     Participants must conform to facilities management procedures in effect at the
                           time of installation.

        4.2. Any organization placing equipment and/or application environments
             at a disaster recovery facility must, at a minimum, ensure adequate
             documentation is provided. This documentation must include:
                4.2.1.     Any reference required to support the stated recovery-time objective (RTO) as
                           outlined in the BIA.

                4.2.2.     Drawings that depict the disaster recovery environment and dependencies on
                           related systems;

                4.2.3.     Environmental requirements (power usage, rack space and other footprint
                           requirements); and

                4.2.4.     Written procedures for performing recovery of the application environment.

        4.3. The standard NJOIT Change Management System must be used for
             installing or modifying equipment and/or applications hosted at the
             disaster recovery facility.
                4.3.1.     A written request must be submitted to the Statewide Disaster Recovery &
                           Planning Team, at oars@oit.nj.gov and datacenter@oit.nj.gov, for a new
                           application environment to be considered for installation within a statewide
                           disaster recovery facility.

                4.3.2.     A minimum of eight weeks lead time should be allowed so the facility
                           Operations Manager can plan and prepare for the installation.

                4.3.3.     A minimum of eight weeks of additional time should be allowed so the facility
                           Operations Manager can test any application or equipment after an
                           installation.

                4.3.4.     For new installations, the request must include the reference information listed in
                           Section V.B. Facilitation and guidance are available to support new
                           installations from the Statewide Disaster Recovery & Planning organization.

5.      RESPONSIBILITIES
        5.1. Chief Technology Officer, Deputy Chief Technology Officers and
             Agency Senior IT Leaders:

07-10-NJOIT, Use of Statewide Disaster Recovery Facilities Policy                                   Page 2 of 4

                5.1.1.     Ensure that OIT and Agency staff are aware and adhere to this policy.

                5.1.2.     Ensure all NJOIT and using departments/agencies cooperate in the execution
                           of the requirements of this policy.

        5.2. Statewide Disaster Recovery & Planning Officer:
        Review and then advise CTO on whether to approve or deny requests for installation of a new
        application environment within a statewide disaster recovery facility.

        5.3. Office of Business Continuity and Disaster Recovery:
        Educate users of the OARS facility about this policy and monitor compliance.

        5.4. Directors, Business Unit Managers and Supervisors:
        Ensure requirements of this policy are fulfilled by the respective agencies and other units of
        State government, and that staff cooperate with the Office of Business Continuity and Disaster
        Recovery in the execution of its responsibilities to this policy.

6.      EXEMPTIONS
        Departments and Agencies shall comply with this policy within 90 days of its effective date.

        A compliance exception must be requested if there is an inability to comply with any portion
        of this policy. Exceptions and noncompliance shall be managed in accordance with Policy 08-
        02-NJOIT 111 - Managing Exceptions.

7.      AUTHORITY
        This policy is established under the authority of N.J.S.A. 52:18A-224 through.52:18A-234. This
        order defines the role of New Jersey’s Office of Information Technology (NJOIT) with regards to
        regarding technology within the community of the Executive Branch of State Government.

        The Office of Information Technology (OIT) reserves the right to change or amend this policy.

07-10-NJOIT, Use of Statewide Disaster Recovery Facilities Policy                                  Page 3 of 4

8.         ADMINISTRATION
           This Policy is administered and monitored by the CTO at 300 Riverview Plaza, Trenton, NJ 08625.

           The Policy must be reviewed annually; however, the CTO reserves the right to change or amend
           the Policy at any time.

           Signature on File                                                12/13/2024
           Christopher J. Rein, Chief Technology Officer                    Date

9.         DOCUMENT HISTORY
 Version      Published Date     CTO         Sections Modified          Description of Modifications
     1.0        06/11/2007                                                Original Published Date
     2.0        06/11/2014
     3.0        12/13/2024      C. Rein              N/A              Annual Review, Updated Format

07-10-NJOIT, Use of Statewide Disaster Recovery Facilities Policy                                   Page 4 of 4

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
