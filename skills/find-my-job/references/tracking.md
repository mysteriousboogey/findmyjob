# Local tracking contract

Use session state unless the user consents to persistent local storage. When consent is given, use the private workspace created by `$setup-find-my-job`; never write candidate data into the plugin or a Git checkout.

Track the canonical vacancy key, source and application URLs, verification time, match evidence, and this lifecycle:

`discovered → verified → shortlisted → approved_for_preparation → preparing → ready_for_user_review → user_confirmed_submitted → interview | rejected | withdrawn | closed`

Opening or filling a form is not submission. Set `user_confirmed_submitted` only after the user says they personally submitted it.

Use canonical keys to suppress duplicates across searches and scheduled runs. Let the user export or delete their locally stored profile and history.
