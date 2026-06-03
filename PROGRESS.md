# PROGRESS.md — Running Coaching Log

Updated by the coach after each review session. Do not edit manually.

---

## Style debts — status

| Habit | First flagged | Last seen | Status |
|-------|--------------|-----------|--------|
| Trailing semicolons | duplicate-integer | top-k-elements-in-list | 🔴 recurring |
| Shadowing builtins (`map`, `list`) | duplicate-integer | top-k-elements-in-list | 🔴 recurring |
| `range(len())` instead of `enumerate` | duplicate-integer | string-encode-and-decode | 🔴 recurring |
| Two-pass when one-pass works | two-integer-sum | two-integer-sum | 🔴 recurring |

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
| Two Pointers (inward scan) | is-palindrome, two-integer-sum-ii | 🟡 building — independent correct implementation in sub-2 (after watching algorithm), directional logic understood |
| Hash set for sequence membership / start detection | longest-consecutive-sequence | 🔴 shaky — sub-1 independent correct O(n log n); O(n) set trick looked up |
| Multi-dimensional constraint hashing (tuple keys) | valid-sudoku | 🔴 shaky — rows/cols independent; box indexing formula and single-pass approach looked up |

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

---

## Coach observations
<!-- append after each session, newest first -->

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
