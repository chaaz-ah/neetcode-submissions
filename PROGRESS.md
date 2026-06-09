# PROGRESS.md — Running Coaching Log

Updated by the coach after each review session. Do not edit manually.

---

## Style debts — status

| Habit | First flagged | Last seen | Status |
|-------|--------------|-----------|--------|
| Trailing semicolons | duplicate-integer | top-k-elements-in-list | 🟡 improving — not seen since is-palindrome |
| Shadowing builtins (`map`, `list`, `sum`) | duplicate-integer | trapping-rain-water | 🔴 recurring — `sum` shadowed in sub-1 |
| `range(len())` instead of `enumerate` | duplicate-integer | trapping-rain-water | 🔴 recurring — sub-1 right-pass uses `range(len(height), 0, -1)` (also OOB); positive sign: left-pass used `enumerate` correctly |
| Two-pass when one-pass works | two-integer-sum | two-integer-sum | 🔴 recurring |
| Index-as-value bug (`for i in coll: use coll[i]`) | two-integer-sum-ii | trapping-rain-water | 🔴 recurring — **third appearance** in sub-1 (`for i in water: sum += water[i]`) |
| Pointer movement inside conditional branch | max-water-container | max-water-container | 🟡 improving — not seen since |
| Misnaming variables (`minArea` while tracking max) | max-water-container | max-water-container | 🟡 improving — not seen since |
| Stale loop variable reuse (`value` from enumerate borrowed in second loop) | trapping-rain-water | trapping-rain-water | 🟡 new — sub-1 |
| `[] * n` instead of `[0] * n` for list init | trapping-rain-water | trapping-rain-water | 🟡 new — sub-1 |

Status key: 🔴 recurring · 🟡 improving · 🟢 fixed (seen clean for 3+ problems)

---

## Pattern recognition — what's landed

| Pattern | Problems seen | Confidence |
|---------|--------------|------------|
| Hashmap for O(1) lookup | duplicate-integer, is-anagram, two-integer-sum, anagram-groups | 🟡 building |
| Hash set for "have I seen this before?" | duplicate-integer | 🟡 building |
| Character counting (array vs hashmap) | is-anagram, anagram-groups | 🟡 building |
| One-pass complement search | two-integer-sum | 🔴 shaky — two-pass used in sub-1/sub-2 |
| Canonical key grouping (defaultdict) | anagram-groups | 🔴 shaky — solution looked up, defaultdict not yet understood |
| Frequency map + rank extraction (top-k) | top-k-elements-in-list | 🔴 shaky — counting step solid, extraction (sort/heap/bucket) all looked up |
| Min-heap for top-k (heapq) | top-k-elements-in-list | 🔴 shaky — used in sub-2 but pruning vs extraction pops not yet understood |
| Length-prefix encoding / framing | string-encode-and-decode | 🔴 shaky — length-prefix instinct correct but all 3 correct subs looked up |
| Prefix products (left × right decomposition) | products-of-array-discluding-self | 🔴 shaky — right instinct in sub-1 but broken implementation; sub-3/4 are looked-up solution |
| Two Pointers (inward scan) | is-palindrome, two-integer-sum-ii, max-water-container, three-integer-sum | 🟡 building — three correct independent implementations now (palindrome sub-2, two-sum-ii sub-2, max-water sub-2 with hint); scaffolding owned, decision rule per-problem still needs verbal precision |
| Hash set for sequence membership / start detection | longest-consecutive-sequence | 🔴 shaky — sub-1 independent correct O(n log n); O(n) set trick looked up |
| Multi-dimensional constraint hashing (tuple keys) | valid-sudoku | 🔴 shaky — rows/cols independent; box indexing formula and single-pass approach looked up |
| Two Pointers — greedy "move the bottleneck side" | max-water-container, trapping-rain-water | 🟡 building — same rule applied in sub-3 (trapping-rain-water); looked up |
| Sort + fix-one + two-pointer with dedup (3Sum-style) | three-integer-sum | 🔴 shaky — sub-6 algorithm correct but dedup mechanics (outer skip + inner skip after match) explicitly not understood per comments |
| Set-of-tuples for dedup of unordered triples | three-integer-sum | 🟡 building — sub-3/4 correct independent use of `set.add(tuple(...))` carrying anagram-groups syntax knowledge |
| Prefix-suffix max decomposition | trapping-rain-water | 🔴 shaky — correct structure attempted in sub-1 but six implementation bugs; sub-2 is correct looked-up solution; same two-pass shape as products-of-array |

Confidence key: 🔴 shaky · 🟡 building · 🟢 solid

---

## Problem log

| Problem | Submissions | Notes written | Revisit? |
|---------|-------------|---------------|----------|
| duplicate-integer | 3 (2 Java, 1 Python) | 2026-05-13 | not marked |
| is-anagram | 4 (Python) | 2026-05-13 | not marked |
| two-integer-sum | 3 (Python) | 2026-05-13 | not marked |
| anagram-groups | 4 (Python) | 2026-05-14 | marked — redo in 1 week |
| top-k-elements-in-list | 4 (Python) | 2026-05-18 | marked — redo in 1 week |
| string-encode-and-decode | 6 (Python) | 2026-05-22 | marked — redo in 1 week |
| products-of-array-discluding-self | 5 (Python) | 2026-05-26 | marked — redo in 1 week |
| is-palindrome | 5 (Python) | 2026-06-03 | not marked |
| longest-consecutive-sequence | 3 (Python) | 2026-06-03 | not marked |
| valid-sudoku | 3 (Python) | 2026-06-03 | not marked |
| two-integer-sum-ii | 3 (Python) | 2026-06-03 | not marked |
| three-integer-sum | 7 (Python) | 2026-06-06 | marked — redo in 1 week |
| max-water-container | 3 (Python) | 2026-06-06 | not marked |
| trapping-rain-water | 4 (Python) | 2026-06-09 | marked — redo in 1 week |

---

## Coach observations
<!-- append after each session, newest first -->

*2026-06-09 — trapping-rain-water (4 subs). **Sub-0** independent attempt — wrong mental model: used immediate neighbors (`i-1`, `i+1`) instead of global left/right maxima, and `max(water, maxWater)` instead of summing. "bruh idk." **Sub-1** watched a video then tried prefix/suffix max arrays — structure correct, implementation broken in six ways: `[] * n` is `[]` (not `[0] * n`); `maxLeft[i] = value` stores current element instead of running max `left`; right-pass range starts OOB at `len(height)` instead of `n-2`; second loop uses stale `value` from the enumerate loop above instead of `height[i]`; `maxRight[i] = value` instead of `right`; `for i in water: sum += water[i]` iterates values as indices — **third appearance of this bug** (two-integer-sum-ii sub-0, three-integer-sum adjacent, and here). Also shadows `sum`. Positive: used `enumerate` correctly in the left pass — the `range(len())` habit may be weakening. **Sub-2** correct O(n) prefix/suffix looked up from "other vids" — clean, no debts, comment says "ts is so hard." **Sub-3** correct O(1) two-pointer, also looked up. Assist levels: sub-0 independent (broken), sub-1 watched video (broken), sub-2/3 looked up. New style debts flagged: `[] * n` vs `[0] * n`; stale loop variable reuse. New SYNTAX.md entry: `[0] * n` list initialization. Pattern: prefix-suffix decomposition added (🔴 shaky — same two-pass shape as products-of-array, but sub-1 couldn't implement it). **max-water-container and three-integer-sum "What made it click" still blank** — flagged again at top of notes.*

*2026-06-06 — three-integer-sum (7 subs) and max-water-container (3 subs) reviewed. **three-integer-sum**: long arc — sub-0/1 tried two-pointer shape without prerequisites (no sort, no inner loop, index-as-value bug — same bug shape as two-integer-sum-ii sub-0, so flagging it as a recurring debt). Sub-2 was a broken O(n³) brute force that excluded valid triplets like `[0,0,0]` via pairwise inequality. Sub-3/4 reached correct O(n³) with sort + `set.add(tuple(...))` — the tuple-as-key syntax from anagram-groups carrying over independently is a real win. Sub-5 is a byte-duplicate of sub-4. Sub-6 is NeetCode's O(n²) two-pointer; algorithm correct, but comments explicitly say "dont get lines 6-7" (outer dedup skip) and "dont get why we do the following" (inner skip-loop after match) — the entire dedup mechanism is the gap. Also missing symmetric `e`-side dedup (only dedups `s`); still correct but extra work. Assist level: sub-0/1 independent (broken), sub-2 independent (broken), sub-3/4/5 partial-lookup ("looked solution a little"), sub-6 looked up. **max-water-container**: clean progression — sub-0 independent O(n²) brute force ("did this on my own lol"), sub-1 two-pointer attempt with two real bugs (`(s-e)` makes width negative so `if` branch never fires; pointer movement is inside `else:` so it freezes once area improves; ties cause infinite loop), sub-2 correct O(n) with hints. Sub-2 comment says "the hint that you should move the larger height was monumental" — but the code moves the *smaller* pointer (correct rule). Either the wording is off or the rule is backward in their head; called out at length in notes. Assist level: sub-0 independent, sub-1 independent (broken), sub-2 watched algorithm + hint. Two new SYNTAX.md entries: `max(best, x)` for running max, and list/set/dict mutator cheatsheet. Two Pointers pattern confidence upgraded — three correct independent implementations across is-palindrome/two-integer-sum-ii/max-water-container; scaffolding owned, per-problem decision rule still needs verbal precision. **"What made it click" still blank** across all of is-palindrome, longest-consecutive-sequence, valid-sudoku, two-integer-sum-ii — flagged at top of three-integer-sum notes. Two-integer-sum-ii's `while s <= e` question also unanswered — flagged.*

*2026-06-03 — two-integer-sum-ii reviewed. 3 submissions (Python). Sub-0 had a classic "iterate values, use them as indices" bug (`for i in numbers` → `numbers[i]`). Sub-1 patched to correct indexing but stayed O(n²) — sorted constraint completely unused. Sub-2 is a correct two-pointer implementation done independently after watching the algorithm walk-through; comment confirms ownership ("implemented this by myself"). Minor issue in sub-2: three `if` branches instead of `elif` — no wrong answers but one extra comparison per iteration. Assist level: sub-0/1 independent (broken) / sub-2 watched algorithm then implemented independently. Two Pointers confidence upgraded to 🟡 building. `range(len())` debt still visible in sub-1. valid-sudoku "What made it click" still blank — flagged again at top of notes.*

*2026-06-03 — longest-consecutive-sequence and valid-sudoku reviewed (both missing notes). longest-consecutive-sequence: 3 submissions. Sub-0 genuine attempt — correct sort-based structure but streak never resets between sequences (bug), dead `else: continue`. Sub-1 independent fix — correct O(n log n) sort with duplicate-skip and proper streak reset; solid work. Sub-2 is the O(n) set solution with the `num - 1 not in numSet` start-check trick — no comment, jumped straight from working O(n log n) solution, likely looked up. valid-sudoku: 3 submissions. Sub-0 independent — rows and cols correct, comment explicitly says "idk how to do 3x3". Sub-1 added box logic after seeing solution — rows/cols independent, box formula (`(square // 3) * 3 + i`) looked up. Sub-2 copied the single-pass defaultdict with `(r // 3, c // 3)` tuple key. Key thing to internalize on both: the start-check trick in LCS and the box-key formula in sudoku. No new SYNTAX.md entries — tuple key already documented from anagram-groups. `range(len())` style debt visible again in valid-sudoku sub-0.*

*2026-06-03 — is-palindrome reviewed. 5 submissions (Python). First Two Pointers problem — new pattern category. Sub-0/1 were genuine independent attempts: core idea correct (filter → lowercase → reverse-compare) but used `isalpha()` which misses digits, shadowed the Python builtin `reversed`, left dead code (`print` after `return`), and used verbose `if x: return True; return False` instead of `return x`. Sub-2 independently caught the digit gap and fixed it with `isalpha() or isnumeric()` — right diagnosis, `isalnum()` is the clean version. Subs 3 and 4 are looked-up solutions: sub-3 is the clean string-build with `isalnum()`, sub-4 is the optimal two-pointer (with manual `ord()` checks — user's own comment "too much js" shows they knew it was off). Assist level: sub-0/1 independent (syntax lookup) / sub-2 independent (self-corrected) / sub-3/4 looked up. Two SYNTAX.md entries added: `isalnum()` and `reversed` builtin shadowing. Style debts: no trailing semicolons or `range(len())` this session — possible improvement there. `reversed` shadowing is a new variant of the builtin-shadowing habit. products-of-array "What made it click" still blank — flagged again in is-palindrome notes.*

*2026-05-26 — products-of-array-discluding-self reviewed. 5 submissions (Python). Sub-0 was a correct brute force O(n²) with ChatGPT assist. Sub-1 was an independent attempt at the prefix/postfix approach after watching NeetCode's algorithm explanation — right instinct, broken in two ways: prefix/postfix arrays store individual values instead of running products, and `i != 0 | i != len(nums)-1` has an operator precedence bug (`|` over `!=`) that makes the condition always False. Sub-2 retreated to O(n²) brute force — no comment. Subs 3 and 4 are the NeetCode O(n) scalar prefix/postfix solution, identical, both correct. Assist level: sub-0 ChatGPT assisted / sub-1 watched algorithm then implemented independently (broken) / sub-2 unclear / sub-3/4 looked up solution. `range(len())` debt still present in sub-0/1/2. One SYNTAX.md entry added: `|` (bitwise OR) vs `or` (boolean OR) — sub-1's boundary bug. string-encode-and-decode "What made it click" still blank — flagged again. Revisit marked for 1 week.*

*2026-05-22 — string-encode-and-decode reviewed. 6 submissions (Python). Sub-0 was an independent attempt using space as delimiter — encode was complete, decode threw a NameError on undefined `letter`. Sub-1 was ChatGPT-assisted, still broken (can't mutate `i` inside a Python `for` loop). Sub-2 was ChatGPT-solved decode — structurally clean but space-delimiter approach is semantically wrong for strings containing spaces. Subs 3/4/5 are all NeetCode length-prefix solutions: sub-3 had a missing `i += 1` after comma parsing, sub-4 fixed it, sub-5 is the cleaner `len#str` interleaved format. Assist level: sub-0 independent (broken) / sub-1 ChatGPT assisted (broken) / sub-2 ChatGPT solved (wrong approach) / sub-3/4/5 looked up solution. `range(len())` debt still present in sub-0/1/2. One SYNTAX.md entry added: `dict.items()` vs `range(len())` — user explicitly asked for this in top-k notes. top-k "Your turn" partially answered (`.items()` insight correct); "What made it click" still blank — flagged again. Revisit marked for 1 week.*

*2026-05-18 — top-k-elements-in-list reviewed. 4 submissions (Python). Sub-0 was an independent attempt — defaultdict used correctly for freq counting (anagram-groups pattern carried over, which is a real win), but extraction logic is fundamentally broken: iterates `range(len(freq))` against a non-integer-indexed defaultdict, and `value = i` tracks the index rather than the frequency. All three style debts (trailing semicolons, builtin shadowing `list = []`, `range(len())`) present in sub-0. Subs 1, 2, 3 all looked at the solution — sorting, heap, and bucket sort approaches respectively. Sub-2 comment shows the two-heappop pattern wasn't understood. Assist level: sub-0 independent (broken) / sub-1/2/3 looked up solution. One SYNTAX.md entry added: heapq min-heap pattern. Revisit marked for 1 week. "Your turn" sections across all problems (duplicate-integer through anagram-groups) are still largely blank — flagged again in top-k notes.*

*2026-05-14 (re-review) — anagram-groups notes updated. "Your turn" was blank despite COACH.md requiring pre-fill from submission comments — fixed. Content seeded from: sub-0 comment (char map, stalled on grouping strategy), sub-2 comment (GPT-assisted), sub-3/sub-5 (explicit defaultdict and tuple gaps). Revisit marked. "Your turn" sections across ALL prior problems (duplicate-integer, is-anagram, two-integer-sum, anagram-groups) still need the user to fill in their own reflection — the pre-fills are seeds, not answers.*

*2026-05-14 (second) — anagram-groups reviewed. 4 submissions. Sub-0 was a genuine attempt that stalled before a grouping strategy landed. Sub-2 reached the correct approach (sorted key) but comment confirms GPT-assisted ("kinda asking gpt to fix a lot of the errors"). Sub-3 and sub-5 are NeetCode solutions — comments on both explicitly say "i do not know what a defaultdict is" and ask about tuple/list(values()). Assist level: looked up solution. Two new SYNTAX.md entries added: tuple() as dict key, dict.values() + list(). Builtin shadowing (`map`) still showing up — that's four problems in a row now. "Your turn" sections across all previous problems (duplicate-integer, is-anagram, two-integer-sum) are still blank as of this session.*

*2026-05-14 — Scheduled check-in. No new submissions since initial bulk sync. Notes are written and complete for all three problems. The "Your turn" sections in every notes.md are still blank — that reflection is the whole point of the exercise, and it's the one thing that hasn't happened yet. Until those are filled in, the learning is only half-done. Next session: check if "Your turn" got filled in, and flag it again if not.*

*2026-05-13 — Coach notes written for all three problems: duplicate-integer, is-anagram, two-integer-sum. All four style debts active (trailing semicolons, builtin shadowing, range(len()), two-pass preference). Two Sum one-pass complement pattern is the key thing to internalize. Initial PROGRESS.md setup.*
