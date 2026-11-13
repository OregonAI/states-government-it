type: Fixed

Seed list: a `slice: {section_start, section_end_before}` is accepted on an entry of any state (it was Oklahoma only), another state's slice shape on an Oklahoma entry now fails the check, and the ingester refuses a sliced HTML source whose state hook would commit the whole page (as it already refused a sliced PDF it cannot cut).
