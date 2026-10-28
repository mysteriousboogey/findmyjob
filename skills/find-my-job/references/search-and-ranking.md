# Search and ranking contract

## Query plan

1. Build queries from each target title or qualification cluster, location, arrangement, and hard exclusions.
2. Search company career sites and/or job boards according to the candidate's source preference.
3. Search recent results first, using a seven-day filter when the source supports it.
4. Open the vacancy page. A search snippet alone does not confirm a match.
5. Cross-check aggregators against the employer's page when possible.

## Confirm before ranking

A listing is confirmed only when its page is reachable and shows an active application path or an unambiguous open status. Record:

- normalized company and title for deduplication
- source URL and direct application URL
- observed open status and verification date
- posting date or `Not stated`
- exact salary wording or `Not advertised`
- arrangement and location as advertised
- public recruitment contact or `Not publicly listed`
- evidence for each hard requirement

Treat “competitive”, estimates from another site, and inferred market ranges as `Not advertised`. Never convert annual to monthly salary unless clearly labelled as a calculation, and do not use a calculation to pass a hard salary floor.

## Deduplicate and rank

Deduplicate by normalized company + title + location, preferring the employer's canonical application page. Keep alternate sources only as verification notes.

Exclude unconfirmed listings and hard-criteria failures. Rank the rest by:

1. hard-criteria confidence
2. remote-first when requested
3. posted within 7 days
4. preferred criteria such as salary, benefits, source, and arrangement
5. older verified-open listings

Do not pad the table. Fewer confirmed matches is better than invented or weak matches.

## Commute evidence

Commute origin and search location are different fields. A place name or straight-line distance does not prove walking time. Use a current routing/map source for the walking leg and full journey. Disclose transfers, assumed station, route time, and anything that could not be checked. Never state a commute as confirmed from an office postcode alone.
