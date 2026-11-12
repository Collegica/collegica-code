# Where the data goes: notes

Anthropic's privacy centre and the Claude Code data page, read as the pages'
own text. The Consumer Terms and the Privacy Policy themselves were **not**
read.

## Training

<https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training>,
read 2026-11-10 (page dated 16 March 2026; it names "Claude Free, Pro, Max"
and has not been updated to mention Ultra).

- "We will use your chats and coding sessions (including to improve our
  models) if: You choose to allow us to use your chats and coding sessions to
  improve Claude"; if "Your conversations are flagged for safety review"; or
  by "explicitly opting in".
- What is included: "the entire related conversation, along with any
  content, custom styles or conversation preferences, as well as data
  collected when using Claude for Chrome. It does not include raw content
  from connectors (e.g. Google Drive), including remote and local MCP
  servers, though data may be included if it's directly copied into your
  conversation".
- "Your Incognito chats are not used to improve Claude, even if you have
  enabled Model Improvement in your Privacy Settings."
- Thumbs up or down: "we will store the entire related conversation … for up
  to 5 years".

<https://claude.com/pricing>, read 2026-11-10: comparison table, "Model
training": **"Opt-out"** on Free, Pro, Max and Ultra. Team: "No model
training on your content by default".

<https://code.claude.com/docs/en/data-usage>, read 2026-11-10:

- "Consumer users (Free, Pro, Max, and Ultra plans): We give you the choice
  to allow your data to be used to improve future Claude models. We will
  train new models using data from Free, Pro, Max, and Ultra accounts when
  this setting is on (including when you use Claude Code from these
  accounts)."
- "Privacy settings can be changed at any time at
  claude.ai/settings/data-privacy-controls."

**Not established from a page read:** whether the switch is on or off for an
account that has never touched it. "Opt-out" on the pricing page says on; no
page read states the default in a sentence. It is on the *For the owner*
list.

## How long it is kept

<https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data>,
read 2026-11-11 (page dated 1 July 2026).

- A deleted conversation is "Removed from your chat history immediately" and
  "Deleted from our back-end storage systems within 30 days".
- With the training setting on: "we may retain your data in a de-identified
  format for up to 5 years in our model training pipelines. This retention
  period only applies to new or resumed chats after the model training
  setting has been enabled."
- Turning it off: "we will not use your previous or new chats or coding
  sessions for future model training … Your data will still be included in
  model training runs that are already in progress, or in models that have
  been trained."
- Flagged content: "inputs and outputs for up to 2 years and trust and safety
  classification scores for up to 7 years".
- Feedback and bug reports: 5 years.

Claude Code data page (as above): "Users who allow data use for model
improvement: 5-year retention period"; "Users who don't allow data use for
model improvement: 30-day retention period".

## Claude Code on your own computer

<https://code.claude.com/docs/en/data-usage>, read 2026-11-10.

- "Claude Code runs locally. To interact with the LLM, Claude Code sends
  data over the network. This data includes all user prompts and model
  outputs".
- "Claude Code clients store session transcripts locally in plaintext under
  `~/.claude/projects/` for 30 days by default to enable session
  resumption." "Transcripts of sessions started or most recently continued
  in Claude Desktop or Cowork are exempt from that limit by default".
- `/feedback` (also `/bug`, `/share`): "a copy of your conversation history
  including code is sent to Anthropic", "retained for 5 years".
- The session survey's follow-up ("Can Anthropic look at your session
  transcript…"): "Yes" uploads the transcript, "retained for up to 6
  months"; "Nothing is uploaded unless you explicitly select Yes."
- Telemetry: metrics "never include your code, prompts, or file paths";
  `DISABLE_TELEMETRY=1` and `DISABLE_ERROR_REPORTING=1` turn them off.
- Cloud sessions: "Your repository is cloned into the session's isolated VM.
  Anthropic stores the session transcript".

Seen in the tests, 2026-11-11: each `claude -p` run left a transcript folder
under `~/.claude/projects/`, named after the test folder's path.
