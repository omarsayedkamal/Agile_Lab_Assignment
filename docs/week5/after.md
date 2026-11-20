# Before and after

| Measure | Before (`legacy_fees.py`) | After (`fees.py`) |
|---|---:|---:|
| Ruff issues | 16 (as stated in the lab handout; verify with your installed Ruff) | Not measured in this build environment; run `ruff check .` locally and record the result. |
| Highest cyclomatic complexity | 9 (`calc`, as stated in the handout) | Not measured here; record the result from Ruff/Pylint if your configuration reports it. |
| Main calculation arguments | 6 (`calc`) | 5 (`tuition_fee`, including optional values) |
| Pylint score | Not captured; see `before.txt` | Not captured; run `pylint week5/fees.py`. |
| Tests passing | 0 in the handout's legacy starting point | 22 passed in the prepared project (`pytest -q`). |

## Pairing reflection — personalize before submitting

I worked through the kata by checking the grade boundaries instead of testing only typical scores. During the refactoring, I kept the original fee calculation available and used tests to check that the new version preserved its existing results. The tests also helped expose the scholarship-student bug in the old loop. I would still like to review the changes with a teammate before merging, especially the naming and fee-reporting choices.

**Important:** The reflection above describes individual preparation, not a pair session. Since no partner participated, do not submit it as evidence that pair programming or a partner review took place. If your instructor requires genuine pairing, contact your instructor or arrange a real review and update this paragraph to describe what actually happened.
