# Response to optional methodology checker suggestions

Date: 15 October 2026.

Role disclosure: the methodology reviewer switched to implementation assistant after delivering the independent review. This response records implementation and self-tests; it is not a fresh independent review or a change to the earlier assessment. Only root working copies were edited. No frozen assessment bundle, release-preparation file, mathematical statement or proof was changed.

## Changes

- W1 — `vector_exact.py`: retained the nine cell-probability validity checks, then independently recomputed the four-category row means, centered residual variances, all six directed margins and direct four-score gap. Added ten explicit-exception checks: D scaling, N scaling, residual scaling, six positive scaled margins and direct-score agreement/negativity. The categorical check counter is 19 total (nine existing plus ten added). Exact scale is `1/200`; categorical gap is `-708952329/823900000000`.
- W2 — `completion_exact.py`: added a two-row compatible equal-mean fixture with common and private columns: channel rows `(1/2,1/2,0)` and `(1/2,0,1/2)`; supported target values `(0,1,_)` and `(0,_,1)`. Both means equal `1/2`; the single-knot completion `(0,1,1)` certifies coefficient zero. Eight added checks cover means, all-zero completion margins, four posteriors including singletons, direct no-disclosure gap, and rejection of a corrupted shared coordinate.
- W3 — `test_sharp_coefficient.py` now refers directly to the integrated manuscript's full-support sharp-coefficient section, not an unavailable historical fragment. `README_V3.md` removes the absent historical program reference, explains the retained legacy invocation warning, and describes the new regression coverage without claiming new universal results.

## Executed tests

From `[local project root]`, executed both `python3 -B SCRIPT` and `python3 -B -O SCRIPT` for each script below. All eight commands exited zero with matching normal/optimized results.

| Script | Result in each mode |
|---|---|
| `verify_release.py` | 600 directions; 586 negative witnesses; 140 positive posteriors; 57 sparse edges; 4 invalid inputs; 3 negative controls; invokes 45-check sharp suite |
| `test_sharp_coefficient.py` | 45 checks, unchanged numerical results |
| `completion_exact.py` | 2,045 checks, up from 2,037; coefficient `16/9` and limiting ratio `160000/90009` unchanged |
| `vector_exact.py` | Original six margins and vector residual unchanged; 19 categorical checks pass, including ten new checks |

The sharp suite's nested and standalone runs are duplicate coverage, not independent evidence. These are exact arithmetic regressions, not formal proof verification. `-B` suppressed bytecode-cache writes. The frozen final bundle's 15-entry `MANIFEST.sha256` still passes after implementation.

## Revised working-file SHA-256

| File | SHA-256 |
|---|---|
| `vector_exact.py` | `39f4c54e9cbfc6dda976e017e44ccee44e97b53e7e1a1da656ba35b01a7f74d8` |
| `completion_exact.py` | `b183b2012c3bab6d4ff665e5102e950f1876b81173aabf62f6e5fff45801d74b` |
| `test_sharp_coefficient.py` | `91102abf9e1df22f84ffcacacc005b8e8d07664e73fe8f79f437595d5c25c411` |
| `README_V3.md` | `548e35d8de075604432884e07fe3363336c151f9c9aac63ad7de72a94f530810` |
