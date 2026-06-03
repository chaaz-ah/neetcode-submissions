# Valid Anagram (NeetCode 242) — Coach Notes

- **Problem:** https://leetcode.com/problems/valid-anagram/
- **Pattern:** Arrays & Hashing
- **Difficulty:** Easy
- **Your submissions:** 4 (all Python)

---

## Honest verdict

Four submissions, all functionally correct, exploring genuinely different approaches. **This is the right way to grind a problem** — solve it, then ask "can I do it differently?" Real credit for that. Now let's pick each apart.

## Submission-by-submission

*All four bulk-synced 2026-05-13 from NeetCode. Future submissions will get per-commit timestamps.*

### `submission-0.py` — two-map hashmap — *2026-05-13 13:04*

```python
seen = {}
teen = {}                       # cute, but rename: `t_count` is clearer
for char in s:
    if char in seen:
        seen[char] += 1;        # trailing semicolons — Python doesn't use them
    ...
return teen == seen
```

- **Works.** Two maps, compare at end.
- **Missing length check.** If lengths differ they can't be anagrams — bail in O(1) instead of doing two full passes. You added this later. Good.
- **Style:** `seen`/`teen` is funny; `s_count`/`t_count` reads better. Drop the trailing semicolons.
- **Time:** O(n + m). **Space:** O(n + m), or O(1) if guaranteed lowercase ASCII (bounded by 26 keys).

### `submission-1.py` — sort-and-compare — *2026-05-13 13:04*

```python
if len(s) != len(t):
    return False
return sorted(s) == sorted(t)
```

- Length check added ✓
- Cleanest code of the four.
- **Trade-off:** O(n log n) vs O(n) — slower than the hashmap. In interview, mention the trade explicitly.
- **Space:** O(n) — `sorted()` returns a new list.

### `submission-2.py` — one-pass dict counter — *2026-05-13 13:04*

```python
mapS, mapT = {}, {}
for i in range(len(s)):
    mapS[s[i]] = 1 + mapS.get(s[i], 0)
    mapT[t[i]] = 1 + mapT.get(t[i], 0)
return mapS == mapT
```

- **Single loop now** because the length check guarantees equal length.
- **`.get(key, 0)`** is good Pythonic. Even cleaner: `from collections import defaultdict; mapS = defaultdict(int); mapS[c] += 1`.
- **Time:** O(n). **Space:** O(n), bounded by alphabet.

### `submission-3.py` — array counter (best one) — *2026-05-13 13:04*

```python
count = [0] * 26
for i in range(len(s)):
    count[ord(s[i]) - ord('a')] += 1
    count[ord(t[i]) - ord('a')] -= 1
for val in count:
    if val != 0:
        return False
return True
```

- **The interview-favorite version.** Constant space, increment-then-decrement trick.
- **Time:** O(n). **Space:** O(1).
- **Constraint to state aloud:** *"This assumes lowercase English. For Unicode I'd switch to a hashmap."*

## Interview scorecard (would you have gotten the offer?)

- **Correctness:** ✓ — all four pass
- **Optimal complexity reached:** ✓ — sub-3 is genuinely optimal (O(n)/O(1))
- **Time/space stated unprompted:** ✗ — no comments anywhere
- **Brute force first:** ✓ (loose) — sub-0 isn't textbook brute force, but you started with a "obvious" approach (two maps) before optimizing
- **Edge cases discussed before coding:** ✗ — you only added the length check after sub-0. Should have been there from the start.
- **Communication while coding:** ✗ — no comments, no narration trace
- **Follow-up question prep:**
  - *"What if the strings contain Unicode (emoji, accents)?"* → Array counter (sub-3) breaks. Hashmaps (sub-0, sub-2) still work because they're not bounded to 26 keys.
  - *"What if you can't use any extra space?"* → Sort approach is O(1) extra if you can mutate; otherwise no purely O(1) is possible without modifying input.
  - *"What if you needed to check if any permutation of `s` appears in `t`?"* → That's Permutation in String, a sliding window of size `len(s)` over `t` with a rolling Counter.

**Verdict:** **hire** on sub-3 alone — that's the canonical optimal. The lack of comments and edge-case discussion knocks it down from "strong hire." **Sub-3 is the version to memorize as your default for any "compare strings by frequency" problem.**

**What to say out loud in this interview:**
- > "Edge cases: different lengths → automatically False. Empty strings → both are vacuously anagrams of each other, return True."
- > "Naive: sort both, compare. O(n log n)."
- > "Better: count characters. With a fixed alphabet of 26, I can use an array instead of a hashmap — O(1) space."
- > "Trick: increment for s, decrement for t. If they're anagrams, all counts end at zero."
- > "Time O(n), space O(1). For Unicode I'd swap the array for a hashmap."

## The most pythonic version (worth knowing)

```python
from collections import Counter
return Counter(s) == Counter(t)
```

In an interview, **mention it as the one-liner**, then immediately offer to implement it from scratch. Showing that you know the stdlib AND can do it manually is the strongest signal.

## Style fixes (apply going forward)

1. **Drop trailing semicolons.** `return True` not `return True;`. Same advice as your other notes.
2. **Don't shadow builtins.** Not flagged here, but watch in other problems (`map`, `list` in two-integer-sum).
3. **Use `enumerate(s)` instead of `range(len(s))`** when you need index + value:
   ```python
   for i, ch in enumerate(s):                # ✓
       count[ord(ch) - ord('a')] += 1
   ```

## The pattern this teaches

**Character counting via hashmap or fixed-size array.** When comparing two collections by frequency, your tools:
- `Counter` (most idiomatic)
- `dict` with `.get()` or `defaultdict`
- Fixed-size array if alphabet is bounded (best constant space)

The **increment-then-decrement** trick from sub-3 is generalizable — appears in sliding window problems (Permutation in String, Find All Anagrams).

## Your journey

| | |
|---|---|
| **Problem in this repo** | #2 (Arrays & Hashing — same family as #1) |
| **Patterns reused** | hashmap counting (1st time) — distinct from set-dedup in Contains Duplicate, but cousin pattern |
| **Clicking** | exploring multiple approaches on the same problem before moving on — exactly right |
| **Shaky** | edge cases not stated up front (had to *discover* the length check by writing sub-0 without it) · trailing semicolons (still) |

**Growth:** four genuine variations on one problem is real exploration — way more than just "solve and move on." But compared to Contains Duplicate (#1) you didn't waste attempts on broken syntax this time. The mix-of-approaches habit is good — keep it for medium-difficulty problems where the trade-offs matter more.

## Question for you

If `s` and `t` contained Unicode (emoji, accents, Chinese), **which of your four solutions would still work without modification?**

> (Answer: 0, 1, 2 — sub-3 is the only one that hard-codes alphabet size. Worth knowing why before you reach Group Anagrams.)

## Your turn — fill this in

**What I tried first (before the working ones):**

**Why I tried 4 different approaches:**

**Which one would I reach for first if I saw this in an interview, and why:**

**Revisit?** [ ] Mark if I want to redo this from scratch in 1 week, *without looking at my code.*
