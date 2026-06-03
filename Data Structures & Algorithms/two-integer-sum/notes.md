# Two Sum (NeetCode 1) — Coach Notes

- **Problem:** https://leetcode.com/problems/two-sum/
- **Pattern:** Arrays & Hashing
- **Difficulty:** Easy
- **Your submissions:** 3 (all Python)

---

## Honest verdict

The progression here — **brute force → hashmap with a real bug → bug caught and fixed** — is the most instructive moment in your whole repo so far. Catching your own bug between submission-1 and submission-2 is the actual job of being an engineer. That said, your final version is still two passes when one will do, and you have a recurring habit of shadowing Python builtins. Let's lock both of those in before they become hard to unlearn.

## Submission-by-submission

*All three bulk-synced 2026-05-13 from NeetCode. Future submissions will get per-commit timestamps.*

### `submission-0.py` — brute force, slightly broken — *2026-05-13 13:04*

```python
for i in range(len(nums)):
    for j in range(1, len(nums)):       # ← bug: should be range(i+1, len(nums))
        if i != j:
            if nums[i] + nums[j] == target:
                list = [i, j];          # ← `list` is a Python builtin, don't shadow it
                return list;
# ← no `return []` at the end
```

Three issues:
1. **Inner loop starts at `1`, not `i + 1`** — you check every pair twice. Still works, but 2× slower than necessary and signals "I haven't fully thought about the loop bounds."
2. **`list = [i, j]`** — `list` is a builtin Python type. Inside this function it's mostly harmless, but it's a habit that *will* burn you elsewhere (try doing `list("abc")` after assigning `list = [...]` — error).
3. **No fallback `return`.** Returns `None` if no pair found. LeetCode guarantees a solution so it passes, but defensively wrong.

**Complexity:** O(n²) time, O(1) space.

### `submission-1.py` — hashmap, with a real bug — *2026-05-13 13:04*

```python
map = {};                                # ← `map` is also a builtin
for i in range(len(nums)):
    map[nums[i]] = i;
for i in range(len(nums)):
    comp = target - nums[i]
    if comp in map and comp != nums[i]:  # ← BUG: compares values, should compare indices
        return [i, map[comp]];
```

**The bug walked through on `[3, 3]`, `target = 6`:**
- `i = 0`, `comp = 3`. `comp in map` ✓. But `comp != nums[i]` → `3 != 3` → False. Skipped.
- `i = 1`, same. Skipped. Returns nothing.

You wanted "don't pair an element with itself" — but the right check is *don't pair an element with itself by **index***, not by value. Index check: `map[comp] != i`. You caught this in the next submission, which is the win of the whole repo.

### `submission-2.py` — bug fixed, correct — *2026-05-13 13:04*

```python
map = {};
for i in range(len(nums)):
    map[nums[i]] = i;
for i in range(len(nums)):
    comp = target - nums[i]
    if comp in map and map[comp] != i:   # ← fixed
        return [i, map[comp]];
return [];
```

Correct. **Time:** O(n). **Space:** O(n). But still two passes when one will do.

## Interview scorecard (would you have gotten the offer?)

Scoring against a senior FAANG-level bar — code working is the floor.

- **Correctness:** ✓ — final solution passes
- **Optimal complexity reached:** partial — O(n)/O(n) is optimal in the unsorted case, but you used **two passes when one suffices.** An interviewer notices.
- **Time/space stated unprompted:** ✗ — no comments declaring complexity. Add them inline next time.
- **Brute force first:** ✓ — you wrote O(n²) in sub-0 before optimizing. **This is genuinely good** and what a real interview wants.
- **Edge cases discussed before coding:** ✗ — the `[3, 3]` duplicate case is the single most common interview trap on this problem and you only caught it by failing the test. In an interview, you should *say* "what if there are duplicates?" before writing a single line.
- **Communication while coding:** unknown (no comments) — practice narrating: "*I'm storing each value mapped to its index. Then for each element I compute what I need to find..."*
- **Follow-up question prep:**
  - *"What if the array is sorted?"* → Two pointers, O(n) time, **O(1) space**. (That's literally the next problem: Two Sum II.)
  - *"What if you need to return all pairs, not just one?"* → Same hashmap, but accumulate into a result list instead of early-returning.
  - *"What if the array doesn't fit in memory?"* → External sort then two-pointer scan.

**Verdict:** **lean hire** on the final code. The bug-catching is a real positive signal, but the missing edge-case discussion and the two-pass-when-one-suffices would drop you below "strong hire." In a real interview you'd want to be at the level of:

```python
def twoSum(self, nums, target):
    # O(n) time, O(n) space. One pass — we only need to check
    # against indices we've already seen, so duplicates are handled naturally.
    seen = {}                                 # value -> index of values already passed
    for i, num in enumerate(nums):
        comp = target - num
        if comp in seen:                      # comp is guaranteed at a different index
            return [seen[comp], i]
        seen[num] = i                         # add AFTER the check
    return []
```

Why this version is interview-stronger:
- One pass instead of two
- The `if comp in seen` *before* `seen[num] = i` makes the no-self-pairing correctness obvious without needing an index check
- The comment declares complexity unprompted
- The variable name `seen` is descriptive and doesn't shadow a builtin

**What to say out loud in this interview** (memorize these phrasings):
- > "Brute force is O(n²) — nested loops. Can we do better? The repeated work is the inner loop's search. A hashmap turns that O(n) lookup into O(1)."
- > "Before I code: edge cases are empty array, single element, and duplicates. The duplicates case is interesting — `[3, 3]` with target 6 should return `[0, 1]`."
- > "I'll do one pass. For each element, I check if its complement is already in the map; if so, return. Otherwise, store the current element. The 'check before store' order guarantees we never pair an element with itself."
- > "Time O(n) — one pass. Space O(n) — worst case the map holds all elements before finding the pair."

## Style fixes (apply going forward)

1. **`map = {}` → `seen = {}`.** Don't shadow builtins. (Same fix flagged in your other notes.)
2. **`list = [i, j]` → `return [i, j]`.** Same reason.
3. **Drop trailing semicolons** — `return x;` → `return x`. No Python writes those.
4. **`for i in range(len(nums))` → `for i, num in enumerate(nums)`** when you need both. Faster, more readable, and signals Python fluency.

## The pattern this teaches

**Hashmap complement search.** This is THE pattern of Arrays & Hashing — probably the most reused pattern in the whole NeetCode 150. The shape is always:

> *"For each element, what would I need to pair with it? Have I already seen that?"*

You'll meet variations soon:
- **3Sum** — fix one element, then Two Sum on the rest
- **4Sum** — fix two elements, then Two Sum on the rest
- **Subarray Sum Equals K** — for each prefix sum `cur`, check if `cur - k` is in the map of prefix sums seen
- **Longest Substring Without Repeating Characters** — "have I seen this char in my current window?"
- **Contains Duplicate** (which you just did) — degenerate case: complement *is* the value itself

Get *very* comfortable with the one-pass shape above. It's a template you'll reuse a dozen times.

## Your journey

| | |
|---|---|
| **Problem in this repo** | #3 (Arrays & Hashing, all 3 so far) |
| **Patterns reused** | hashmap-complement (1st time), hash-set-for-dedup (used in Contains Duplicate) |
| **Clicking** | reaching for dict/set on "have I seen this" is becoming default |
| **Shaky** | loop-bound hygiene (`range(1, n)` here, `i > n - 2` in Contains Duplicate Java) · shadowing builtins (`map`, `list`) |

**Growth:** sub-1 → sub-2 was a *debug*, not a rewrite — you found `comp != nums[i]` was wrong on `[3, 3]` and fixed it precisely. That's a real step up from Contains Duplicate where you bailed from Java to Python instead of debugging the syntax. Do more of this.

## Question for you

You wrote the two-pass version. The one-pass version doesn't need the `map[comp] != i` index check — it's just `if comp in seen`. **Why is the one-pass version automatically safe from the duplicate trap?**

> Write the answer in your "Your turn" section below. If you can articulate it, you've genuinely learned the pattern — not just the problem.

## Your turn — fill this in

**What I tried first:**

**What was I thinking when I wrote `comp != nums[i]` in sub-1 — and what tipped me off to fix it in sub-2?**
> The bug-catching moment matters more than the final code. Two minutes on this.

**Why does the one-pass version not need the `!= i` check?** (Answer to the question above.)
> If you can write this in plain English, the pattern is yours.

**One thing I want to do differently on my next Arrays & Hashing problem:**

**Revisit?** [ ] Mark to redo from scratch in 1 week.
