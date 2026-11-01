# Candidate profile contract

Extract only job-relevant facts directly supported by the resume or the user's corrections:

- name and contact details for later form preparation
- location when stated
- education, qualifications, field, and dates
- employment, internships, projects, responsibilities, and dates
- skills, tools, certifications, licences, languages, and stated proficiency
- achievements exactly as supported
- explicit career objective or target role

For every material fact retain a provenance label: `resume`, `user_confirmed`, `user_corrected`, or `calculated`. Label calculated durations and show their source dates. Mark unclear or conflicting values for confirmation instead of resolving them silently.

Present a compact review grouped by contact, education, experience, skills, certifications, languages, and unresolved items. The user may confirm all, correct fields, add missing facts, remove facts, or provide another resume.

Resume possession authorizes reading for the requested job search, not persistent storage or employer disclosure. Ask immediately before saving outside the conversation and state the location. Never store credentials or place candidate data in the plugin repository.
