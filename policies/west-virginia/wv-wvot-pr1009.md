---
schema_version: 1
corpus: states-government-it
jurisdiction: west-virginia
id: wv-wvot-pr1009
title: Vulnerability Assessment and Remediation Procedure
doc_type: policy
citation: WVOT-PR1009
authority_level: ''
issuing_body: West Virginia Office of Technology (Chief Information Officer)
source_url: https://drive.google.com/uc?export=download&id=1lbEpL3DmrbyAqsa1B5B4zF_VKtZsfkvU
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 422cc15b59ddba5420cf2c1e3f2402e1861e339871df364d83a26ecee16821f5
effective_date: null
source_version: Revised 03/13/2026
status: current
content_mode: verbatim
conversion_notes: Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). Google Drive's PDF puts a zero-width space (U+200B) around runs of text; they are kept as
  extracted. source_version is the revision or issue date the policy prints, as printed.
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
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Vulnerability Assessment and Remediation Procedure (WVOT-PR1009)

## At a glance

Requirements for information security vulnerability assessments and remediation on the executive domain (listed under Procedures on the index). The index also lists an older 'Vulnerability Scanning' 2012 version of the same number, left out as superseded.

## Full text

I​ssued by the​                            ​Vulnerability Assessment and Remediation Procedure​
 ​Chief Information Officer​                                                    ​WVOT-PR1009​

                                                                                                      ​ 1/01/2012​
                                                                                                      1
                                                                                             ​Revised 03/13/2026​
                                                                                     ​OPR: WVOT Cybersecurity​
                     ​COMPLIANCE WITH THIS PUBLICATION IS MANDATORY​
                              ​ ublications are available online at:​
                              P
 ​https://sites.google.com/wv.gov/wvot-extranet/policy-governance/executive-branch-policies​
​ uestions​ ​and​ ​change​ ​recommendations​ ​related​ ​to​ ​this​ ​publication​ ​shall​ ​be​ ​directed​ ​to​ ​this​
Q
​publication's​ ​Office​ ​of​ ​Primary​ ​Responsibility​ ​(OPR).​ ​This​ ​publication​ ​shall​ ​be​​reviewed​​every​
 ​two​ ​years​ ​to​ ​ensure​ ​continued​ ​alignment​ ​with​ ​current​ ​legal,​ ​operational,​ ​and​ ​strategic​
  ​requirements. Revisions will be undertaken as necessary.​

​SUMMARY OF VERSIONS AND CHANGES​
 ​Version​          ​Date​              ​Revision Description​

                    ​03/13/2026​        ​Reformatted and updated web links and reporting process​

  ​1.​   ​PURPOSE​

         ​1.1.​     ​ his​ ​procedure​ ​establishes​ ​standardized​ ​requirements​ ​and​ ​expectations​ ​for​
                    T
                    ​Information​ ​Security(IS)​ ​vulnerability​​assessments​​and​​remediation​​in​​regards​​to​
                     ​the State of West Virginia’s executive domain and its users.​

  ​2.​   ​SCOPE​

         ​2.1.​     ​ his​ ​procedure​ ​applies​ ​to​ ​all​ ​departments​ ​(including​ ​agencies,​ ​boards,​
                    T
                    ​authorities,​ ​and​ ​commissions)​ ​within​ ​the​ ​Executive​ ​Branch​ ​of​ ​WV​ ​State​
                     ​Government,​ ​excluding​ ​constitutional​ ​officers,​ ​the​ ​WV​ ​Board​ ​of​ ​Education,​ ​the​
                      ​WV​ ​Department​ ​of​ ​Education,​ ​and​ ​the​ ​county​ ​boards​ ​of​ ​education​ ​that​ ​have​
                       ​access​ ​to​ ​or​ ​use​ ​State-provided​ ​resources.​ ​However,​ ​the​ ​WVOT​ ​recommends​
                        ​that all agencies, including those excluded above, follow this procedure.​

         ​2.2.​     ​ here​ ​there​ ​are​ ​procedures​ ​in​ ​place​ ​which​ ​provide​ ​less​ ​restrictions​ ​or​ ​security​
                    W
                    ​than​ ​this​ ​procedure,​ ​those​ ​procedures​ ​will​ ​be​ ​superseded​ ​by​ ​this​ ​procedure.​​In​
                     ​instances​ ​where​ ​existing​ ​state​ ​and​ ​federal​ ​laws,​ ​regulations,​ ​and​ ​policies​ ​are​
                      ​more restrictive than this procedure, the more restrictive provisions will prevail.​

  ​3.​    ​PROCEDURE​
         ​3.1.​     ​Requirements​

                  ​3.1.1.​   ​ nder​ ​the​ ​provisions​ ​of​ ​West​ ​Virginia​ ​Code​ ​§5A-6-4a​ ​et​ ​seq.,​ ​the​ ​Chief​
                             U
                             ​Information​ ​Office​ ​(CIO)​ ​is​ ​charged​ ​with​ ​securing​ ​State​ ​government​
                              ​information​​and​​the​​data​​communications​​infrastructure​​from​​unauthorized​
                               ​uses, intrusions, or other security threats.​

                                                      ​Page​​1​​of 2​

     ​Vulnerability Assessment and Remediation Procedure​
​WVOT-PR1009                              Issue Date: 11/01/2012                         Revised: 03/13/2026​

              ​3.1.2.​   ​ he​ ​WVOT​ ​will​ ​adopt​ ​and​ ​implement​ ​standards,​ ​procedures,​ ​and​ ​best​
                         T
                         ​practices​​to​​minimize​​the​​risk​​of​​security​​breaches​​within​​the​​goals​​of​​this​
                          ​procedure.​​To​​the​​extent​​that​​there​​are​​procedures​​in​​place​​which​​provide​
                           ​less​ ​security​ ​than​ ​this​ ​procedure,​ ​they​ ​will​ ​be​ ​superseded​ ​by​ ​this​
                            ​document.​ ​In​ ​instances​ ​where​ ​existing​ ​state​ ​and​ ​federal​ ​laws​ ​and​
                             ​regulations​ ​are​ ​more​ ​restrictive​ ​than​ ​information​ ​security​ ​policies​ ​and​
                              ​procedures​ ​issued​ ​by​ ​the​ ​WVOT,​ ​the​ ​more​ ​restrictive​ ​provisions​ ​will​
                               ​prevail.​

     ​3.2.​     ​Procedure​

              ​3.2.1.​   ​User Responsibilities:​

                     ​3.2.1.1.​   ​ sers must report any observation of attempted security or privacy​
                                  U
                                  ​violations to:​
                                   ​https://wv.accessgov.com/technology/Forms/Page/incident-reportin​
                                    ​g/incident-reporting/​

                     ​3.2.1.2.​    ​Users​​must​​immediately​​report​​all​​information​​security​​incidents​​to​
                                  ​ ttps://wv.accessgov.com/technology/Forms/Page/incident-reportin​
                                  h
                                  ​g/incident-reporting/​

                     ​3.2.1.3.​   ​Users​ ​must​ ​provide​ ​the​ ​following​ ​information,​ ​to​ ​the​ ​extent​
                                  ​ ossible:​
                                  p

                           ​3.2.1.3.1.​    ​Point​ ​of​ ​contact​ ​(name,​ ​agency,​ ​phone,​ ​cell​ ​number,​
                                           ​ -mail);​
                                           e

                           ​3.2.1.3.2.​    ​Physical location of incident (building, room#, etc.)​

                           ​3.2.1.3.3.​    ​Date and time incident occurred and detected, is it ongoing;​

                           ​3.2.1.3.4.​     ​ escription​ ​of​ ​event​ ​(ex:​ ​unauthorized​ ​access,​ ​system​
                                            D
                                            ​breach​ ​or​​malfunction,​​data​​loss​​or​​exposure,​​defacement,​
                                           ​and any actions taken in response to the incident.​

                           ​3.2.1.3.5.​    ​Description of the extent of impact;​

              ​3.2.2.​   ​Chief Information Security Officer (CISO) Responsibilities:​

                     ​3.2.2.1.​    ​ uthorizing​​scheduled​​and​​random​​use​​of​​information​​security​​and​
                                   A
                                   ​risk​ ​assessment​ ​tools​ ​to​ ​evaluate​ ​State​ ​computer​ ​devices​ ​and​
                                    ​applications.​​This​​will​​include​​testing​​websites​​for​​risk​​vulnerability​
                                  ​as they pertain to confidentiality, integrity, and availability.​

                     ​3.2.2.2.​   ​ oordinating​ ​the​ ​application​ ​of​ ​risk​ ​assessment​ ​tools​ ​with​ ​the​
                                  C
                                  ​Information​ ​Security​ ​Administrator​ ​(ISA)​ ​of​ ​each​ ​agency​ ​owning​
                                   ​the​ ​system,​ ​agency​ ​policy​​influencing​​leaders,​​web​​coordinator(s)​
                                    ​and/or​ ​the​ ​webmaster,​ ​and​ ​the​ ​hosting​ ​agency,​ ​in​ ​order​ ​to​

                                                  ​Page​​2​​of 7​

     ​Vulnerability Assessment and Remediation Procedure​
​WVOT-PR1009                         Issue Date: 11/01/2012                           Revised: 03/13/2026​

                             ​minimize operational disruptions.​

                ​3.2.2.3.​    ​ he​ ​CISO​ ​will​ ​evaluate​ ​all​ ​requests​ ​for​ ​exemption​ ​from​ ​this​
                              T
                              ​procedure.​​Requests​​must​​be​​received​​in​​writing​​and​​signed​​by​​the​
                               ​agency​​ISA​​or​​asset​​manager.​​The​​request​​must​​include​​business​
                                ​reasons​ ​justifying​ ​why​ ​the​ ​risk​ ​assessment​ ​methods,​ ​tools,​ ​and​
                                 ​techniques​ ​should​ ​not​ ​be​ ​employed.​ ​The​ ​CISO​ ​will​ ​decide​ ​each​
                                  ​case​ ​based​ ​on​ ​its​ ​merit;​​appeals​​of​​the​​decision​​may​​be​​made​​to​
                             ​the CIO.​

         ​3.2.3.​   ​WVOT Cybersecurity Office Responsibilities​

                ​3.2.3.1.​    ​ elect​ ​and​ ​use​ ​all​ ​practical​ ​methods,​ ​tools,​ ​and​ ​technologies​ ​to​
                              S
                              ​evaluate​ ​the​ ​security​ ​of​ ​the​ ​State’s​ ​computer​ ​devices​ ​and​ ​the​
                               ​applications​ ​that​ ​run​ ​on​ ​them.​ ​These​ ​may​ ​include,​ ​but​ ​are​ ​not​
                                ​limited​ ​to,​ ​tools​ ​that​ ​scan​ ​for​ ​common​ ​operating​ ​systems​ ​and​
                             ​application configuration and program vulnerabilities.​

                ​3.2.3.2.​    ​ he​​OISC,​​along​​with​​input​​from​​the​​CIO,​​the​​ISA’s,​​lead​​technical​
                              T
                              ​managers​ ​from​ ​the​ ​WVOT,​ ​and​ ​the​ ​Information​ ​Technology​
                               ​Advisory​ ​Council​ ​(ITAC),​ ​will​ ​establish​ ​security​ ​vulnerability​
                                ​standards,​ ​procedures,​ ​and​ ​best​ ​practices​ ​governing​ ​computer​
                             ​applications, chief network systems, and operating systems.​

                ​3.2.3.3.​    ​ onduct​ ​security​ ​assessments​ ​on​ ​all​ ​new​ ​major​ ​applications​ ​in​
                              C
                              ​accordance​ ​with​ ​the​ ​WVOT​ ​PO1025​ ​Assessment​ ​and​
                             ​Authorization Policy.​

                ​3.2.3.4.​    ​ he​ ​Cybersecurity​ ​Office​ ​will​ ​alert​ ​the​ ​agency’s​ ​ISA,​ ​asset​
                              T
                              ​managers,​​and​​the​​policy​​influencing​​leadership​​of​​the​​agency​​that​
                               ​owns​​the​​system,​​when​​a​​critical​​information​​security​​deficiency​​is​
                             ​discovered.​

                      ​3.2.3.4.1.​    ​The​ ​Cybersecurity​ ​Office​ ​will​ ​work​ ​together​ ​to​ ​correct​ ​the​
                                      ​ eficiency in a timely manner.​
                                      d

                      ​3.2.3.4.2.​     ​ t​ ​the​ ​discretion​ ​of​ ​the​ ​CISO,​ ​the​ ​computer​ ​device​ ​or​
                                       A
                                       ​application​ ​may​ ​be​ ​removed​ ​from​ ​service​ ​until​ ​a​
                                      ​satisfactory remediation is implemented.​

                      ​3.2.3.4.3.​     ​ he​ ​Cybersecurity​ ​Office​ ​will​ ​promptly​ ​provide​ ​a​ ​report​ ​to​
                                       T
                                       ​the​ ​agency​ ​ISA,​ ​asset​ ​managers,​ ​policy​ ​influencing​
                                      ​leadership, and other designated individuals.​

                ​3.2.3.5.​    ​ ybersecurity​​Office​​staff​​will​​protect​​data​​supplied​​to​​evaluate​​risk,​
                              C
                              ​and​​will​​comply​​with​​all​​confidentiality​​requirements​​of​​the​​agency,​
                             ​including signing any necessary contracts/agreements.​

                ​3.2.3.6.​   ​If​ ​the​​Cybersecurity​​Office​​is​​able​​to​​breach​​security​​while​​testing,​

                                             ​Page​​3​​of 7​

     ​Vulnerability Assessment and Remediation Procedure​
​WVOT-PR1009                       Issue Date: 11/01/2012                             Revised: 03/13/2026​

                              t​hey​ ​are​ ​prohibited​ ​from​ ​disclosing​ ​any​ ​confidential​ ​or​ ​personal​
                               ​data,​​or​​the​​source​​of​​the​​vulnerability​​without​​written​​authorization​
                             ​of the CISO and/or Agency Cabinet Secretary.​

         ​3.2.4.​   ​Information Security Administrator (ISA) Responsibilities:​

                ​3.2.4.1.​    ​ ccountable​ ​for​ ​their​ ​agency’s​ ​logical​ ​and​ ​physical​ ​security,​ ​and​
                              A
                             ​will be responsible for the following:​

                ​3.2.4.2.​   ​Implementing risk remediation findings required by the CISO;​

                ​3.2.4.3.​   ​Assisting the CISO in maintaining the State’s information security;​

                ​3.2.4.4.​    ​ nsuring​ ​that​ ​all​ ​relevant​ ​requests​ ​for​ ​proposals​ ​(RFP)​ ​and​
                              E
                              ​resulting​ ​contracts​ ​with​ ​vendors​ ​contain​ ​language​ ​intended​ ​to​
                             ​enforce this procedure and its standards.​

                ​3.2.4.5.​   ​Assessing​ ​potential​ ​risks​ ​in​ ​existing​ ​systems​ ​and​ ​determining​
                             ​ hich should be evaluated for vulnerabilities and remediation.​
                             w

         ​3.2.5.​   ​West Virginia Office of Technology Staff Responsibilities:​

                ​3.2.5.1.​    I​mplementing​ ​the​ ​security​ ​vulnerability​ ​standards​ ​governing​
                               ​WVOT’s​ ​applications,​ ​enterprise​ ​network​ ​systems,​ ​and​ ​operating​
                             ​systems;​

                ​3.2.5.2.​    ​ ssisting​ ​the​ ​CISO​ ​in​ ​the​ ​conduct​ ​of​ ​his/her​ ​duties​​regarding​​the​
                              A
                             ​implementation of this procedure and its standards;​

                ​3.2.5.3.​   ​Remediating critical vulnerabilities within 10 days upon discovery;​

                ​3.2.5.4.​   ​Remediating high vulnerabilities within 20 days upon discovery;​

                ​3.2.5.5.​   ​Drafting a plan of action for medium vulnerabilities;​

                ​3.2.5.6.​    ​Regularly​​assessing​​security,​​and​​remediating​​vulnerabilities​​within​
                             t​heir area of responsibility;​

                ​3.2.5.7.​    ​ lerting​ ​the​ ​CISO​ ​and​ ​the​ ​CIO​ ​when​ ​security​ ​vulnerabilities​
                              A
                              ​beyond​ ​the​ ​scope​ ​of​ ​their​ ​responsibility​ ​are​ ​discovered​ ​or​
                             ​suspected; and​

                ​3.2.5.8.​    ​ lerting​ ​the​ ​CISO​ ​and​ ​the​ ​CIO​ ​of​ ​any​ ​remediation​ ​actions,​
                              A
                              ​highlighting​ ​issues​ ​that​ ​they​ ​may​ ​not​ ​be​ ​able​ ​to​ ​correct,​ ​and​
                               ​documenting​ ​steps​ ​taken​ ​by​ ​using​ ​the​​WVOT’s​​SOC​​remediation​
                             ​tracking system.​

         ​3.2.6.​   ​All IT Vendors/Contractors Responsibilities:​

                ​3.2.6.1.​   ​ ust​ ​agree​ ​to​ ​recognize​ ​the​ ​State’s​ ​right​ ​to​ ​conduct​ ​vulnerability​
                             M
                             ​testing​ ​in​ ​accordance​ ​with​ ​this​ ​procedure,​ ​and​ ​must​ ​agree​ ​to​
                                             ​Page​​4​​of 7​

        ​Vulnerability Assessment and Remediation Procedure​
​WVOT-PR1009                               Issue Date: 11/01/2012                             Revised: 03/13/2026​

                                     ​ upport​ ​vulnerability​ ​testing​ ​and​ ​collaborate​ ​with​ ​the​ ​State​ ​to​
                                     s
                                     ​implement​ ​security​ ​remediation​ ​findings​ ​in​ ​applications​ ​for​ ​which​
                                      ​they​ ​are​ ​responsible.​ ​With​ ​respect​ ​to​ ​systems​ ​implemented​
                                       ​following​ ​the​ ​adoption​ ​of​ ​this​ ​procedure,​ ​in​ ​accordance​ ​with​ ​the​
                                    ​terms of their contract(s), vendors/contractors must agree:​

                            ​3.2.6.1.1.​      t​o​​provide​​a​​secure​​hosting​​environment​​for​​the​​contracted​
                                             ​application;​

                            ​3.2.6.1.2.​      t​o​ ​support​ ​periodic​ ​vulnerability​ ​testing​ ​conducted​ ​by​ ​the​
                                             ​State and/or its agents; and​

                            ​3.2.6.1.3.​     ​to​ ​remediate​ ​significant​ ​security​ ​vulnerabilities​ ​in​ ​a​ ​timely​
                                             ​ anner for the term of the contract.​
                                             m

 ​4.​   ​POLICY-SPECIFIC DEFINITIONS​

        ​4.1.​   ​ ccess–​​The​​ability​​to​​locate,​​gain​​entry​​to,​​and​​use​​a​​directory,​​file,​​or​​device​​on​
                 A
                 ​a computer system or over a network.​

        ​4.2.​   ​ ccess​ ​Controls​ ​–​ ​The​ ​enforcement​ ​of​ ​specified​ ​authorization​ ​rules​ ​based​ ​on​
                 A
                 ​positive​ ​identification​ ​of​ ​users​ ​and​ ​the​ ​systems​ ​or​ ​data​ ​they​ ​are​ ​permitted​ ​to​
                  ​access.​

        ​4.3.​   ​Authentication – The process of verifying the identity of a user.​

        ​4.4.​   ​ hief​ ​Information​ ​Security​ ​Officer​ ​(CISO)​ ​–​ ​Person​ ​designated​ ​by​ ​the​ ​CIO​ ​to​
                 C
                 ​oversee​ ​information​​security​​practices​​and​​initiatives​​for​​the​​Executive​​Branch​​of​
                  ​WV State government, excluding the constitutional officers.​

        ​4.5.​   ​ hief​ ​Technology​ ​Officer​ ​(CIO)​ ​–​ ​The​ ​person​ ​responsible​ ​for​ ​the​ ​State’s​
                 C
                 ​information resources.​

        ​4.6.​   ​ onfidential​ ​Data​ ​–​ ​Information​ ​that​ ​is​ ​legally​ ​protected​ ​(ex:​ ​Protected​ ​Health​
                 C
                 ​Information)​​or​​otherwise​​deemed​​by​​a​​qualified​​expert​​to​​be​​unsuitable​​for​​open​
                  ​access.​

        ​4.7.​   ​Contractor – Anyone who has a contract with the State or one of its entities.​

        ​4.8.​   ​ ustodian​ ​of​ ​Information​ ​–​ ​The​ ​person​ ​or​ ​unit​ ​assigned​ ​to​ ​supply​ ​services​
                 C
                 ​associated with the data.​

        ​4.9.​   ​ mployee​ ​–​ ​Individuals​ ​retained​ ​and​ ​authorized​ ​on​ ​a​ ​temporary​ ​or​ ​permanent​
                 E
                 ​basis​ ​by​ ​the​ ​State​ ​of​ ​West​ ​Virginia​ ​to​ ​perform​ ​a​ ​service.​ ​For​ ​the​ ​purposes​ ​of​
                  ​information​ ​technology​​and​​security​​policy,​​the​​term​​“employee”​​shall​​include​​the​
                   ​following:​​contractors,​​subcontractors,​​contractors’​​employees,​​volunteers,​​county​
                    ​health​ ​department​ ​staff,​ ​business​ ​associates,​ ​and​ ​any​ ​other​ ​persons​ ​who​ ​are​
                     ​determined​ ​and​ ​notified​​by​​the​​WVOT​​to​​be​​subject​​to​​this​​policy.​​This​​definition​
                      ​does not create any additional rights or duties.​

                                                    ​Page​​5​​of 7​

     ​Vulnerability Assessment and Remediation Procedure​
​WVOT-PR1009                            Issue Date: 11/01/2012                            Revised: 03/13/2026​

    ​4.10.​   I​nformation​ ​Assets​ ​–​ ​Any​ ​of​ ​the​ ​data,​ ​hardware,​ ​software,​ ​network,​
               ​documentation, and personnel used to manage and process information.​

    ​4.11.​   ​Information Resources – All information assets, in all known formats.​

    ​4.12.​   I​nformation​​Security​​–​​Those​​measures,​​procedures,​​and​​controls​​that​​provide​​an​
               ​acceptable​ ​degree​ ​of​ ​safety​ ​for​ ​information​ ​resources,​ ​protecting​ ​them​ ​from​
                ​accidental or intentional disclosure, modification, or destruction.​

    ​4.13.​   I​nformation​​Security​​Administrator​​(ISA)​​–​​The​​person​​designated​​by​​the​​agency​
               ​head​ ​to​ ​assure​ ​the​ ​agency’s​ ​compliance​ ​with​​State​​information​​security​​policies​
                ​and​​procedures.​​The​​ISA​​is​​the​​agency’s​​internal​​and​​external​​point​​of​​contact​​for​
                 ​all information security matters.​

    ​4.14.​   I​nformation​ ​Security​ ​Incident​ ​–​ ​An​ ​event​ ​characterized​ ​by​ ​unexpected​ ​and​
               ​unwanted system behavior, breach, or unintended alteration of data.​

    ​4.15.​   I​nformation​ ​Security​ ​Liaison​ ​(ISL)​ ​-​ ​Employees​ ​assigned​ ​by​ ​the​​ISA​​to​​assist​​in​
               ​the protection of information resources.​

    ​4.16.​   I​nformation​​Technology​​(IT)​​–​​The​​technology​​involved​​with​​the​​transmission​​and​
               ​storage​ ​of​ ​information,​ ​especially​ ​the​ ​development,​ ​installation,​ ​implementation,​
                ​and management of computer systems and applications.​

    ​4.17.​   ​ edium​ ​–​ ​Any​ ​repository,​ ​including​ ​paper,​ ​used​ ​to​ ​record,​ ​maintain,​ ​or​ ​install​
              M
              ​information or data.​

    ​4.18.​   ​ wner​ ​of​ ​Information​ ​–​ ​The​ ​person(s)​ ​ultimately​ ​responsible​ ​for​ ​an​ ​application​
              O
              ​and its data viability.​

    ​4.19.​   ​ assword​​–​​A​​string​​of​​characters​​known​​to​​a​​computer​​system​​or​​network​​and​​to​
              P
              ​a​ ​user​ ​who​ ​must​ ​enter​ ​the​ ​password​ ​in​ ​order​ ​to​ ​gain​ ​access​ ​to​ ​an​ ​information​
               ​resource.​

    ​4.20.​   ​Personally Identifiable Information (PII) –Includes all protected and non-​

    ​4.21.​   ​ rotected​​information​​that​​identifies,​​or​​can​​be​​used​​to​​identify,​​locate,​​or​​contact​
              p
              ​an individual.​

    ​4.22.​   ​ rivacy​ ​Officer​ ​-​ ​The​ ​official​ ​responsible​ ​for​ ​facilitating​ ​the​ ​Executive​ ​Branch's​
              P
              ​integration​ ​of​ ​privacy​ ​principles,​ ​legal​ ​requirements,​ ​and​ ​privacy​ ​standards​ ​into​
               ​department policies, procedures, and practices.​

    ​4.23.​   ​ rocedure​​–​​A​​set​​of​​instructions​​or​​process​​steps​​prescribed​​in​​sufficient​​detail​​in​
              P
              ​order​ ​to​ ​understand​ ​how​ ​to​ ​meet​ ​a​ ​policy​ ​requirement.​ ​Procedures​ ​should​
               ​document​ ​roles,​ ​methods,​ ​options,​ ​and​ ​examples​ ​necessary​ ​for​ ​a​ ​reader​ ​to​
                ​understand how to comply with a policy.​

    ​4.24.​   ​Risk​ ​Analysis​ ​–​ ​The​ ​evaluation​ ​of​ ​system​ ​assets​ ​and​ ​their​ ​vulnerabilities​ ​to​

                                                 ​Page​​6​​of 7​

         ​Vulnerability Assessment and Remediation Procedure​
​WVOT-PR1009                                 Issue Date: 11/01/2012                           Revised: 03/13/2026​

                    ​threats in order to identify what safeguards are needed.​

        ​4.25.​     ​Security Contact – These individuals include the ISA or the ISL.​

        ​4.26.​     ​ hreat​ ​–​ ​Includes​ ​any​ ​person,​ ​condition,​ ​or​ ​circumstance​ ​that​ ​endangers​ ​the​
                    T
                    ​security​ ​of​ ​information​ ​or​ ​information​ ​systems​ ​in​ ​the​ ​context​ ​of​ ​information​
                     ​security.​

        ​4.27.​     ​User – A person authorized to access an information resource.​

        ​4.28.​     ​User id – A unique “name” by which each user is identified to a computer system.​

        ​4.29.​     ​ est​ ​Virginia​ ​Division​ ​of​ ​Personnel​ ​–​ ​A​ ​division​ ​of​ ​the​ ​Department​ ​of​
                    W
                    ​Administration​ ​established​ ​by​ ​West​ ​Virginia​ ​Code​ ​§​ ​29-6-1​ ​et​ ​seq.,​ ​which​ ​is​
                     ​responsible​ ​for​ ​the​ ​system​ ​of​ ​human​ ​resource​ ​management​ ​for​ ​operating​
                      ​agencies​ ​in​ ​the​ ​classified​ ​and​ ​classified-exempt​ ​service​ ​of​ ​West​ ​Virginia​ ​State​
                       ​government.​

        ​4.30.​     ​ est​ ​Virginia​ ​Office​ ​of​ ​Technology​ ​(WVOT)​ ​-​ ​The​ ​division​ ​of​​the​​Department​​of​
                    W
                    ​Administration​ ​established​ ​by​ ​WV​ ​Code​ ​§​ ​5A-6-4a,​ ​et.​​seq.,​​which​​is​​led​​by​​the​
                     ​State’s​ ​CIO​ ​and​ ​designated​ ​to​ ​acquire,​ ​operate,​ ​and​ ​maintain​ ​the​ ​State’s​
                      ​technology​​infrastructure.​​The​​WVOT​​is​​responsible​​for​​evaluating​​equipment​​and​
                       ​services, and reviewing information technology contracts.​

 ​5.​    ​RELEVANT MATERIALS AND DOCUMENTS​

         ​5.1.​     ​This policy is consistent with the following federal and state authorities:​

                  ​5.1.1.​   ​NIST SP 800-14 and NIST SP 800-53​

                  ​5.1.2.​   ​W. Va. Code § 5A-6-4a​

                  ​5.1.3.​   ​WVOT PO1025 Assessment and Authorization Policy​

                                                      ​Page​​7​​of 7​

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). Google Drive's PDF puts a zero-width space (U+200B) around runs of text; they are kept as extracted. source_version is the revision or issue date the policy prints, as printed.
