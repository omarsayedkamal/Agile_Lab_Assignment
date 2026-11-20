# Week 5 findings

## Static-analysis findings

The supplied lab handout reports the following Ruff results for the original `legacy_fees.py` (16 findings in total).

| Rule | Count | Smell | Refactoring |
|---|---:|---|---|
| F401 | 2 | Dead code: unused imports | Remove `os` and `math`. |
| PLR2004 | 6 | Magic numbers | Give fee rates, thresholds, surcharges and type values meaningful names; use an enum for student types. |
| C901 | 1 | Complex structure | Replace the nested conditional fee calculation with a rate lookup and a simple sum. |
| PLR0913 | 1 | Too many arguments | Replace the long positional parameter list with clearer domain concepts and defaults. |
| ARG001 | 1 | Unused argument | Remove `y`, because the calculation does not use the year. |
| B006 | 1 | Mutable default argument | Replace `extra=[]` with an immutable tuple default, `extras=()`. |
| E711 | 1 | None comparison | Use a normal truth/default check rather than comparing a value to `None`. |
| E712 | 1 | True comparison | Use `if summer:` rather than `if summer == True:`. |
| F841 | 1 | Unused local variable | Remove `tmp`; its value is never used. |
| N802 | 1 | Invalid function name | Rename `ProcessAll` to `process_all`. |

The handout's exact counts are included as the reference baseline. `docs/week5/before.txt` explains that the actual tool output and Pylint score still need to be captured locally; they have not been fabricated.

## Additional smells Ruff does not explain for us

1. **Unclear names:** `d`, `t`, `s`, `disc`, and `x` make the calculation harder to follow. Names such as `courses`, `student_type`, `summer`, and `discount` communicate intent.
2. **Mixed responsibilities:** `report` both calculates a fee and prints it. Calculation and presentation should be separate so the result can be reused or tested without capturing terminal output.
3. **Duplicated branching:** `ProcessAll` repeats fee-calculation calls for each student type. A single call using the student's actual type is simpler.
4. **Primitive obsession:** course data is represented by dictionaries containing the short key `"h"`, and student types are represented by unexplained integers. A `Course` data class and `StudentType` enum make these concepts explicit.
5. **Unclear unused year parameter:** `y` is accepted by `calc` but does not affect the result, so callers may assume a year-based rule exists when it does not.

## Hidden bug in `ProcessAll`

The function assigns `fee` only when the student's type is 1 or 2. There is no branch for scholarship type 3. When Omar follows Sara, neither condition assigns a new value for Omar, so Python prints the previous loop iteration's `fee` (1050). If Omar is first, `fee` has not been assigned at all and the function raises `UnboundLocalError`. The refactored `process_all` calculates a result for every enum value, so a scholarship student receives 0 rather than inheriting another student's fee.
