# Where the data goes, and the Gemini app

Read 12 November 2026.

| Page | How read | Date on page |
|---|---|---|
| [Google Antigravity Terms](https://antigravity.google/terms) | HTML stripped to text | none found |
| [Antigravity settings](https://antigravity.google/docs/settings), "Data collection settings" and CLI "Enable Telemetry" | Markdown | none |
| [Antigravity FAQ](https://antigravity.google/docs/faq) | Markdown | none |
| [Gemini Apps Privacy Hub](https://support.google.com/gemini/answer/13594961) | summarising fetch, quotes checked against its output only | Privacy Notice updated 13 October 2026; hub 26 October 2026 |
| [Gems in Gemini Apps](https://support.google.com/gemini/answer/15146780) | summarising fetch | — |
| [Google AI plans](https://one.google.com/about/google-ai-plans/) | summarising fetch | — |

## Antigravity

- Terms: "When you use the Service, we record and store your user data,
  interaction data … and any feedback you provide ('Interactions')."
- "We use Interactions to evaluate, develop, and improve Google and Alphabet
  research, products, services and machine learning technologies."
- "Google employees and contractors may access, view, review and use
  Interactions. Please don't submit confidential information or any data
  you wouldn't want a reviewer to see".
- "If you don't want your Interactions used in this way, navigate to
  settings to change your preference … Even when your Telemetry is toggled
  off, Google still uses your data to provide the service, process any
  feedback and help keep Antigravity safe."
- The switch: **Enable Telemetry**, in the app's Settings > Account; in the
  CLI, in `/config`. "When toggled on, Antigravity collects interactions for
  use in evaluating, developing, and improving Antigravity and models"
  (settings page). In the CLI the choice "is saved with your account instead
  of in `settings.json`, and it's always off for business accounts".
- Deleting: by email to the address the terms give (in the terms; not
  repeated here), or in settings for Remote Agents.
- The terms do not say whether telemetry is on by default. Not checked.

## The Gemini app (gemini.google.com and the phone apps)

Not tested. From Google's pages only:

- **Training:** with **Keep Activity** on, "Google uses your activity to
  provide, develop, and improve its services (including training generative
  AI models)." The setting is in Gemini Apps Activity,
  myactivity.google.com/product/gemini.
- **Keeping:** activity auto-deletes after 18 months by default (3 or 36
  months, or never, can be chosen). With Keep Activity off, "Future chats
  are still saved for 72 hours" and are not used for training unless you
  send feedback.
- **People reading chats:** "A subset of chats are reviewed by human
  reviewers"; "Reviewed chats are retained for up to three years", and are
  not deleted when you delete your activity.
- **Temporary Chat:** "not used to train Google's AI models"; kept for 72
  hours.
- **Gems** (saved instructions and files): "Starting in November 2026, Gems
  will go away on personal Google accounts and automatically transition to
  skills." No page on the replacement was read.
- **Memory / saved info:** not read today. For the owner.
