---
schema_version: 1
corpus: states-government-it
jurisdiction: new-york
id: ny-its-g26-002
title: Lake Ontario Map Label Retention
doc_type: policy
citation: NYS ITS Guideline ITS-G26-002
authority_level: ''
issuing_body: New York State Office of Information Technology Services (ITS)
source_url: https://its.ny.gov/lake-ontario-map-label-retention
source_format: pdf
retrieved: '2026-11-11'
source_sha256: a09d35b59eb85a04dea42c6e468c844d4f2ef3ec5b067faebfed885a4f0cfe14
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
- digital-services
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Lake Ontario Map Label Retention (NYS ITS Guideline ITS-G26-002)

## At a glance

Item of the ITS statewide technology policy and standards library (https://its.ny.gov/policies), category 'Policies' on the listing. The listing prints original publication 10/16/2026 and last modified 10/16/2026.

## Full text

                                             State Capitol P.O. Box 2062
                                               Albany, NY 12220-0062
                                                   www.its.ny.gov

        New York State
   Information Technology                        No: ITS-G26-002
          Guideline

              IT Guideline:                      Updated: 10/16/2026

                                                 Issued By: NYS Office of Information
  Lake Ontario Map                               Technology Services
   Label Retention                               Owner: Chief Digital Office

1.0 Purpose and Benefits
On August 27, 2026, U.S. Executive Order 14422 was issued directing U.S.
Federal agencies to rename the geographic feature known as “Lake Ontario” as
“Lake America.” Subsequently, Lake Ontario’s name was changed in the
Geographic Names Information System (GNIS) which is the official Federal source
for geographic names and used in Esri basemaps. As a result, all maps and
applications generated after August 27, 2026 from ArcGIS Online (AGOL), as well
as any applications that are using Esri’s basemaps, and any map applications
using Google Maps could reflect this change.

New York State agencies have been directed by Governor Hochul to continue
using “Lake Ontario.” To ensure consistency, compliance, and control over how
maps display this label, please review and implement the guidance in this
document.

2.0 Authority
Section 103(10) of the State Technology Law provides the Office of Information
Technology Services (ITS) with the authority to establish statewide technology
policies, including technology and security standards. Section 2 of Executive
Order No. 117 1, issued January 2002, provides the State Chief Information Officer

1 All references to Executive Order 117 refer to that which was originally issued by Governor George E.

Pataki on January 28, 2002 and continued by Executive Order 5 issued by Governor Eliot Spitzer on
January 1, 2007, Executive Order 9 issued by Governor David A. Patterson on June 18, 2008, Executive

with the authority to oversee, direct and coordinate the establishment of
information technology policies, protocols and standards for State government,
including hardware, software, security and business re-engineering. Details
regarding this authority can be found in NYS ITS Policy, NYS-P08-002 Authority to
Establish State Enterprise Information Technology (IT) Policy, Standards and
Guidelines.

3.0 Scope
This guideline applies to ITS, its employees, contractors, and consultants and ITS
supported agencies (“Client Agency”).

This guideline applies to Client Agency designated Esri AGOL administrators as
well as application developers using Esri basemaps or Google Maps.

4.0 Information Statement
The following explains the steps ITS and its Client Agencies need to adjust AGOL
sites, AGOL maps and applications, custom applications using Esri basemaps, and
Google Map instances.

4.1     Actions for AGOL Administrators

4.1.1 Change Regional Settings

To prevent unintended label changes on default basemaps, administrators should
adjust the AGOL organization's regional settings from United States to World. This
ensures that default basemaps for new maps and applications will continue to
display "Lake Ontario" where appropriate. To adjust these regional settings, please
follow the steps outlined below:

        1. Log into the AGOL site as an administrator.
        2. Select the Organization > Settings > General.
        3. Under Organization defaults, change the Region to World (the setting
           saves automatically).

Order 2 issued by Governor Andrew M. Cuomo on January 1, 2011 and Executive Order 6 issued by
Governor Kathy Hochul on October 8, 2021.

Reference Number                                                                       Page 2 of 9

Once these regional settings are applied, users will see the correct world basemap
within the AGOL map or application. Please note that if an anonymous user
changes the basemap using the basemap gallery tool, the gallery will display
options based on their physical location, which may result in the “Lake America”
label being shown when a different base map is selected.

To eliminate this issue, administrators can set a custom basemap gallery as the
default and then allow anonymous access to the organization. (Learn more about
anonymous access from guidance available here).

4.1.2 Create Default Basemap Gallery that uses “World” Editions of Esri
      Basemaps

           1. Log in to the AGOL site as an administrator.

           2. From the homepage, click the “Groups” tab in the top toolbar.

           3. Click the [+ Create Group] button (top left).

           4. Use the following text and settings for the new group:

               Name: Basemap Gallery
               Summary: Organizational basemaps using Esri “World” basemaps
               Tags: Basemaps
               Thumbnail: Optional, upload an image for bonus points
               Who can view this group? Everyone (public)
               Who can be in this group? My organization’s members only
               How can people join this group? By invitation
               Who can contribute content? Group owner and managers
               Who can see the full list of members? Group owner and managers
               Group designations: Leave both options disabled

Reference Number                                                        Page 3 of 9

           5. Click the blue “Save” button to finish creating the Group.

           6. Next, click the “Organization” tab in the top toolbar.

           7. Then in the blue toolbar, click “Settings” (to the far right).

           8. In the lefthand navigation bar, click “Map and Scene.”

           9. Under the “Basemap gallery for maps and scenes” section, click on
              the box under “2D Group” (with the pencil icon) and choose the new
              “Basemap Gallery” group that you just made.

Reference Number                                                               Page 4 of 9

           10. Once you set the Basemap Gallery group as the default, click the
               blue button below it that says “Share basemaps.” This will add all the
               default Esri Basemaps (World editions) into your group.

           11. Navigate back to your Basemap Gallery group (Click Groups at the
               top toolbar, then choose the Group from the list).

           12. On the Basemap Gallery group item page, make sure your content
               now includes Esri World Basemaps.

Reference Number                                                           Page 5 of 9

4.1.3 Allow for Anonymous Access to AGOL

           1. Log into the AGOL site as an administrator.

           2. Go to Organization > Settings > Security.

           3. Under the Access and Permissions section, toggle on the option to
              “Allow” anonymous access to your organization’s website.

Combined, the steps outlined in sections 4.1.1-4.1.3 result in the basemaps
showing “Lake Ontario” instead of “Lake America” being publicly available.

4.1.4 Customize your AGOL Homepage

Once anonymous access is enabled, any public user will be able to see the
organization’s homepage and view content that is public. The homepage can be
customized to eliminate sections that are either not relevant to or should be hidden
from anonymous users. To do this, please follow the steps outlined below:

           1. Go to Organization > Settings > General.
           2. Scroll down the options in General until you reach the Navigation
              Bar section.
           3. Click the button to Manage Navigation Bar Links.
           4. In the window that opens, change the selection for any options set to
              “Everyone” to instead be “Organization members” or
              “Organization members who can create.”

4.2    Actions for AGOL Map and Application Owners

4.2.1 Update Maps Applications with your AGOL Organization’s Basemap
      Gallery

Once the AGOL administrator has completed the changes described above,
agency owners of public AGOL maps and applications should check them to
confirm the changes have taken effect. If maps are showing “Lake America”
instead of “Lake Ontario,” the steps below should be followed. Once completed,
maps should be periodically reviewed to ensure continued use of “Lake Ontario.”

           Maps

           1. Open the map's Overview page in AGOL.
           2. Locate and note the current basemap in the Map section of the
              Overview page.
           3. Select Open in Map Viewer.
           4. Open the Basemap tool on the left.

Reference Number                                                          Page 6 of 9

           5. Select the desired basemap (e.g., a custom style or a "World"
              regional basemap) and Save the map to begin using the selected
              basemap.

           Applications

           When setting up widget-based applications like Experience Builder,
           ensure that the basemap widget is configured to use your organization’s
           default basemap gallery. This will ensure the basemap widget displays
           the World basemap collection addressed in steps 4.1.1 and 4.1.2. This
           setting can be found in the map widgets settings.

4.3    Actions for Custom Application Developers

To avoid viewing the recent GNIS name change for Lake Ontario, developers
should refrain from using the Basemap Gallery element. Instead, configure
applications to use either the World Vector Basemaps or the Raster Legacy
Basemaps which are not affected by the GNIS name change.

Note: Raster legacy basemaps are set to retire in 2028/2029

4.4    Google Maps Language Setting for Lake Ontario

To keep the internationally recognized name, “Lake Ontario,” review any
embedded Google Map on your websites and set the Maps language parameter
to “en-CA (Canadian English).” If a map already sets “language=en” or
“language=en-US,” replace it with “en-CA.” The map will stay in English but will

Reference Number                                                         Page 7 of 9

show “Lake Ontario” instead of “Lake America.” After deploying, open the live page,
zoom to the Great Lakes and confirm that the lake is labeled "Lake Ontario."

4.5    Code examples

Script tag
<script
src="https://maps.googleapis.com/maps/api/js?key=YOUR_KEY&callback=initM
ap&language=en-CA"></script>

@googlemaps/js-api-loader
new Loader({ apiKey: "YOUR_KEY", version: "weekly", language: "en-CA" });

Embed iframe

<iframe
src="https://www.google.com/maps/embed/v1/place?key=YOUR_KEY&q=Lake+
Ontario&language=en-CA"></iframe>

5.0 Compliance
This guideline shall take effect upon publication. Compliance with ITS guidelines
is not compulsory, but strongly suggested. ITS may amend its guidelines at any
time; compliance with amended guidelines is not compulsory, but strongly
suggested.

6.0 Definitions of Key Terms
Except for terms defined in this policy, all terms shall have the meanings found in
the ITS Glossary.

7.0 Contact Information
Submit all inquiries and requests for future enhancements to the policy owner at:

                                 Chief Digital Office
                              Reference: ITS-G26-002
                   NYS Office of Information Technology Services
                         State Capitol, ESP, P.O. Box 2062
                               Albany, NY 12220-0062

                            Email: its.dl.cdo-all@ny.gov

Statewide technology policies, standards, and guidelines may be found on the
Policies page of the ITS website.

Reference Number                                                         Page 8 of 9

8.0 Revision History
This guideline should be reviewed consistent with the requirements set forth in
ITS-P24-003 Process for Establishing Information Technology Policies, Standards,
and Guidelines.

 Date              Description of Change                  Reviewer
 10/16/2026        Issued policy                          Chief Digital Office

9.0 Related Documents

Reference Number                                                       Page 9 of 9

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
