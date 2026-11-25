# A guaranteed income floor

Notes behind `website/finance/income-floor/index.md` (finance series item 4).

- `scripts/floor.py` prints every table in the article; `scripts/output.txt`
  is its output. Round numbers, no real person's data.
- Public amounts read from Canada.ca on 2026-11-24: CPP maximum at 65
  $1,507.65 (January 2026), average $858.34 (July 2026); CPP -0.6% a month
  before 65 (max -36%), +0.7% after (max +42%); OAS $762.50 a month at 65 to 74
  (October to December 2026), +0.6% a month deferred up to +36% ($1,037.00).
- Break-even for CPP at 70 versus 65 is computed in real terms with no tax:
  age 82 at 0%, 84 at 2%, 88 at 4% (monthly discounting).
- Annuity payout rates are hypothetical, labelled as such; no quote was
  obtained.

## Not verified

- The residence years needed for a full OAS pension: the article says only
  that it depends on years in Canada, and points to Canada.ca.
- Guaranteed Income Supplement amounts: not used.
- Tax on CPP, OAS and annuity income: ignored in the sums, and the article
  says so.
