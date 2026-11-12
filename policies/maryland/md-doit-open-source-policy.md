---
schema_version: 1
corpus: states-government-it
jurisdiction: maryland
id: md-doit-open-source-policy
title: Maryland Open Source Policy
doc_type: policy
citation: DoIT Maryland Open Source Policy
authority_level: ''
issuing_body: Maryland Department of Information Technology
source_url: https://doit.maryland.gov/policies/Websites-and-Data/Pages/Maryland-Open-Source-Policy.aspx
source_format: html
retrieved: '2026-11-11'
source_sha256: 0af8c18284572dfafef8e8e26507d1475db4063fb7cd1824f03b7166e93075a1
effective_date: null
source_version: ''
status: current
content_mode: verbatim
conversion_notes: Text taken from the page's main content (title and rich-text field) as DoIT's SharePoint
  site serves it, one line per paragraph, heading, list item and table row (a table row's cells are joined
  by ' | '; list items carry a bullet or their number). Links are written as their text, pictures and
  page navigation are not read, and an e-mail address the site obscures prints as '[email protected]'.
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

# Maryland Open Source Policy (DoIT Maryland Open Source Policy)

## At a glance

Listed on DoIT's Websites and Data policies page (https://doit.maryland.gov/policies/Websites-and-Data/Pages/default.aspx). As the page prints its purpose: The Maryland Department of Information Technology (DoIT) is committed to improving how state agencies acquire, build, and deliver information technology (IT) solutions to better support cost efficiency, operational effectiveness, and the public’s experience with government programs.

## Full text

Maryland Open Source Policy
Purpose and Benefits
The Maryland Department of Information Technology (DoIT) is committed to improving how state agencies acquire, build, and deliver information technology (IT) solutions to better support cost efficiency, operational effectiveness, and the public’s experience with government programs.
Currently, when the State develops custom source code, it is not always made available for reuse across agencies. As a result, the State may pay multiple times for similar code, leading to duplicative efforts and inefficient use of taxpayer dollars.
By expanding the reuse of custom-developed code across state government, we can:
• Reduce redundant costs
• Decrease development time
• Avoid vendor lock-in
This policy ensures that custom-developed source code is broadly available for reuse across agencies.
Note: This policy does not require agencies to open source their code—it simply permits and encourages it when appropriate.
Working in the Open
Working in the open means providing public access to your source code during development. This fosters collaboration, transparency, and better software through public feedback.
You should make your code publicly available in a source code repository such as GitHub or Gitlab. This includes code developed by third-party vendors.
When working in the open, we suggest you:
• Use Semantic Versioning to indicate code changes and releases
• Communicate clearly with users via support channels or mailing lists
Creating a new project in the open
It is much easier to write your code in the open from the beginning of a project than it is to open a repository later, because you can address security and other issues as you go along. If you do not do this, you will have to spend a costly period of time at the end of the project checking if your code is all safe to be released.
Coding in the open from the start means you should:
• Plan how you’ll avoid publishing sensitive information later in the project
• Follow best practices from the beginning, for example keeping good documentation
• Set in place processes that will allow you to continuously publish code as it is written
• Allow others to identify parts of your code for reuse which you might not have recognized yourself
• Allow others to contribute ideas as the project is in progress; for example if they know of existing tools that could help
Make sure that:
• The repository’s contents will be publicly releasable under an open license
• The project does not have a special categorical security sensitivity, such as including classified information
• The repository includes a README file with a clear project description; if applicable, these should include installation instructions.
• The project or program manager agrees that the above conditions have been met
Make an existing project open
When making existing code open, you must:
• Code and Legal Reviews
  • Review and remove all personally identifiable information (PII), including private keys, tokens, passwords, IP addresses, and other authentication details.
  • Verify that licenses and contracts governing the project’s contents (including dependencies and third-party libraries) allow public release.
  • Conduct a security review to identify and fix any vulnerabilities.
  • Ensure no inappropriate content (e.g., unprofessional comments) is present in the codebase.
• Documentation and Compliance
  • Include a README file with a clear project description and installation instructions (if applicable).
  • Include a LICENSE file, documenting any third-party code with separate license requirements.
  • Obtain confirmation from the project or program manager that all required steps have been followed.
Reusing third-party code in a Maryland project
In the case of forking a third party’s repository, ensure that:
• The terms under which the source code base is licensed is understood
• The source code base’s license permits modification and re-use
Contributing to a Maryland open source project
Encouraging contributions from people who use your code can help make your code more robust, as people will spot bugs and suggest new features. If you would like to encourage contributions, you should:
• Include contributing guidelines
• Set time aside to maintain your code
• Maintain a public issues list
• Have a strong code review process. For reference, here’s a general set of Code Review Guidelines you can adapt for your team or project.
Also ensure that:
• All PII, including private keys, tokens, passwords, IP addresses, and other authentication information has been removed from any commits
• All of the commits’ contents are allowed to be released under the repository’s existing license
Licensing
Maryland agencies should default to the MIT license unless another Open Source Initiative (OSI)-compatible licensebetter fits the project’s needs.
Documenting Your Projects
To encourage contributions and reuse by the community, it is important for teams to clearly and consistently document their work. 18F, a digital consultancy within the U.S. General Services Administration, has developed an excellent set of guidelines for documenting GitHub-based projects, which the Maryland agencies should use as a reference.

## Curator notes

Text taken from the page's main content (title and rich-text field) as DoIT's SharePoint site serves it, one line per paragraph, heading, list item and table row (a table row's cells are joined by ' | '; list items carry a bullet or their number). Links are written as their text, pictures and page navigation are not read, and an e-mail address the site obscures prints as '[email protected]'.
