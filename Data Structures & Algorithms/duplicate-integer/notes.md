# Contains Duplicate (NeetCode 217) — Coach Notes

- **Problem:** https://leetcode.com/problems/contains-duplicate/
- **Pattern:** Arrays & Hashing
- **Difficulty:** Easy
- **Your submissions:** 3 (2 Java, 1 Python)

---

## Honest verdict

You landed a clean, correct one-liner. But the two broken Java attempts that came first are the more instructive part — they show a specific habit (writing code fast without tracing it on paper) that's worth fixing before it hides bigger bugs later.

## Submission-by-submission

*All three bulk-synced 2026-05-13 from NeetCode. Future submissions will get per-commit timestamps.*

### `submission-0.java` — broken (won't compile) — *2026-05-13 13:04*

Java/Python syntax fusion:

```java
for int i = 0, i > nums.length - 2, i++ {     // missing parens, commas not semicolons
    if i == j:                                  // Python's `:`, not Java's `{}`
```

If you're going to use Java in interviews, drill the syntax. The compiler errors here blocked you from even checking whether the *idea* was right.

### `submission-1.java` — compiles, but logic is broken — *2026-05-13 13:04*

Syntax fixed, still three logic bugs:

1. **`i > nums.length - 2`** — `>` should be `<`. Loop never runs. Function always returns `false`.
2. **Inner loop uses `i`**: `for (int j = 0; i > nums.length - 1; j++)` — used `i` instead of `j`. Infinite loop if it had entered.
3. **`if (i == j)`** — comparing *indices*, should be `nums[i] == nums[j]`.

This is the most important submission to learn from. **Walk through `nums = [1, 2, 3, 1]` on paper before submitting** — it catches all three.

### `submission-2.py` — correct, elegant — *2026-05-13 13:04*

```python
return len(set(nums)) < len(nums)
```

- **Time:** O(n) — building the set
- **Space:** O(n) — worst case all unique
- **Correctness:** ✓

In an interview, **say it out loud before writing it**: *"A set deduplicates, so if the set is smaller than the original list, there's at least one duplicate."* That demonstrates you understand WHY, not just that you know the trick.

## Interview scorecard (would you have gotten the offer?)

- **Correctness:** ✓ — final passes
- **Optimal complexity reached:** ✓ — O(n)/O(n) is optimal
- **Time/space stated unprompted:** ✗ — no comments
- **Brute force first:** ✗ — you jumped to "use set." Interviewer wants to see you derive it: *"brute force is O(n²), but the inner search is repeated work — a set turns it into O(1) lookup."*
- **Edge cases discussed before coding:** ✗ — empty list? single element?
- **Communication while coding:** ✗ — silent, no comments
- **Follow-up question prep:**
  - *"Now do it without `set()`."* → Manual hash set with early exit (snippet below).
  - *"What if memory is the constraint?"* → Sort + adjacent compare. O(n log n) time, O(1) space.
  - *"What if you need the duplicate's value, not just yes/no?"* → Modify the hash-set version to `return n` on hit.

**Verdict:** **lean hire** on the final code. The Python one-liner is fine, but two broken Java attempts before getting there + no narration + no edge case talk would drop the bar in a real interview. **The one-liner alone is a "show off" answer — interviewers want the trade-off discussion.**

**What to say out loud in this interview:**
- > "Brute force is O(n²) — compare every pair. The repeated work is the inner lookup."
- > "A hash set gives us O(1) lookup, so we can do one pass: for each number, is it in the set?"
- > "Edge cases: empty array returns False. Single element returns False. Duplicates anywhere → True."
- > "Time O(n), space O(n) — set holds at most n elements."

## What an interviewer might push on

After the one-liner, expect **"now do it without `set()`."** Have all three of these ready in order:

```python
# 1. Hash set with early exit (slightly better in practice — bails on first dup)
def hasDuplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False
```

```python
# 2. Sorting (O(1) extra space if you can mutate the input)
def hasDuplicate(nums):
    nums.sort()                          # O(n log n)
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False
```

```python
# 3. Brute force — only as the starting point, never the answer
# O(n²) — for every pair, check equality.
```

## Style fixes (apply going forward)

1. **Add inline complexity comments.** `# O(n) time, O(n) space` at the top of `solve()`. Interviewer-friendly.
2. **When you write a one-liner, also write a 2-line *why-it-works* comment.** The one-liner alone reads as "I memorized this."
3. **If you start in language X and switch to Y, that's fine — but commit to Y faster.** Two broken Java attempts is one too many. After sub-0 didn't compile, dropping to Python is the right call. Don't burn another attempt on broken Java.

## The pattern this teaches

**"Have I seen this before?"** A hash set turns that question into O(1). Same trick recurs in:
- Cycle detection in linked lists
- Contains Duplicate II / III (duplicates within a window)
- Longest substring without repeating characters
- Almost any "dedup" or "is X unique" problem

When you see "find/avoid duplicates," default to *hash set unless space is constrained*.

## Your journey

| | |
|---|---|
| **Problem in this repo** | #1 (Arrays & Hashing) — your starting baseline |
| **Patterns reused** | (none yet — first problem) |
| **Clicking** | reaching for `set()` to dedup — good Pythonic instinct |
| **Shaky** | Java syntax fluency · loop-bound hygiene (`i > n-2` instead of `<`) · not tracing code on paper before submitting |

**Growth signal:** *baseline only — this is your starting point.* Compare future problems to this one: do you still take 2 broken attempts before switching gears? Do you still skip edge-case discussion? Watch those.

## Question for you

If the array has **10 billion integers**, too big for a hash set to fit in memory — but you can read it as a sorted stream from disk — what's your approach?

> (Answer: scan adjacent pairs after sorting. That's why approach #2 above is worth knowing — it's the answer when memory is the constraint, not time.)

## Your turn — fill this in

**What I tried first (before the working one):**

**Why did I start in Java and then switch to Python?**
> Worth being honest with yourself. Strategic switch or giving up? Either's fine, just know which.

**What made the Python one-liner click:**

**Revisit?** [ ] Mark if I want to redo this from scratch in 1 week.
