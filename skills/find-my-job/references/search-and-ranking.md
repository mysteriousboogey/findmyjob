# Discovery, verification, and matching contract

## Query plan

Build searches from confirmed titles or qualification clusters, location, arrangement, recency, and hard exclusions. Search employer career sites and public ATS sources as well as allowed job boards. Discover broadly, then verify on the canonical employer page where possible.

## Verification record

A ranked listing needs a reachable page with an active application path or unambiguous open status. Record:

- normalized company, title, and location
- source and direct application URL
- observed open status and verification time
- posting date or `Not stated`
- exact advertised salary or `Not advertised`
- arrangement and location as advertised
- public recruitment contact or `Not publicly listed`
- job description and evidence for each hard requirement

Search snippets can discover but cannot verify a vacancy. Treat “competitive,” third-party estimates, and inferred ranges as `Not advertised`. Do not convert pay periods to pass a hard salary floor.

## Deduplication and eligibility

Use normalized company + title + location as the canonical key, preferring the employer application page. Keep alternate sources only as evidence notes.

For every mandatory criterion record `pass`, `fail`, `needs confirmation`, or `not stated`. Exclude confirmed failures. Do not silently turn unknowns into passes.

## Suitability

Score only eligible jobs using supported evidence for relevant experience, demonstrated skills, education or certification, role and industry alignment, preferences, and evidence strength. Explain strong matches, partial matches, gaps, and unresolved requirements. A score is comparative suitability, not hiring probability.

Rank by eligibility confidence, confirmed user preferences, recency, evidence strength, and older verified-open roles. Do not pad results.

## Commute

Search location and commute origin are separate. Verify walking and full journey times with a current routing source. Disclose assumptions, transfers, source, and verification time. Straight-line distance or a postcode alone is not commute evidence.
