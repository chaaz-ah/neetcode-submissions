# Longest Consecutive Sequence — Coach Notes

- **Problem:** https://leetcode.com/problems/longest-consecutive-sequence/
- **Pattern:** Arrays & Hashing
- **Difficulty:** Medium
- **Submissions:** 3 (Python)

## Verdict

Sub-0 was a genuine attempt but has a real bug — the streak counter never resets when a sequence breaks, so it overcounts across multiple sequences. Sub-1 is an independent fix: correct O(n log n) sort-based solution that handles duplicates and resets the streak properly. Sub-2 is the O(n) set solution — the jump from a working sort-based answer straight to the set trick suggests it was looked up. **Assist level: sub-0 independent (broken) / sub-1 independent (correct, suboptimal) / sub-2 looked up solution.**

---

## Submission-by-submission

### `submission-0.py` — genuine attempt, streak never resets

```python
count = 0
for i in range(1, len(nums)):
    if nums[i] == nums[i-1] + 1:
        count += 1
    else:
        continue
count += 1
return count
```

- `count` accumulates across the entire array and never resets when a sequence breaks. On `[1, 2, 3, 100, 101]` it returns 5 — wrong, longest is 3.
- `else: continue` is a no-op — `continue` here does nothing that the loop wouldn't do anyway.
- No handling for duplicates: `[1, 1, 2]` — `nums[1] == nums[0] + 1` is False (1 ≠ 2), so count stays 0, +1 = 1. Correct by accident, but `[1, 1, 2, 3]` → count is 2 (1→2, 2→3), +1 = 3. Correct again — but the logic is fragile.
- No empty array check.

**Time:** O(n log n) — sort. **Space:** O(1) if sorting in-place.

**Interviewer take:**
- The streak-never-resets bug would be caught immediately with a two-sequence example. Expect: "walk me through `[1, 2, 3, 100, 101]`."
- `else: continue` would prompt "what does that `continue` do here?" — you should catch it yourself before they ask.

---

### `submission-1.py` — correct sort-based solution, independent

```python
if not nums:
    return 0
nums.sort()
res = 0
curr = nums[0]
streak = 0
i = 0
while i < len(nums):
    if curr != nums[i]:
        curr = nums[i]
        streak = 0
    while i < len(nums) and nums[i] == curr:
        i += 1
    streak += 1
    curr += 1
    res = max(res, streak)
return res
```

This is correct. The inner while loop skips duplicates. When `curr != nums[i]`, the sequence broke — `curr` jumps to `nums[i]` and `streak` resets to 0. This is solid independent work: you diagnosed the sub-0 bug and fixed it completely.

The structure is a bit complex — two nested loops, manual `i` management — but it's correct and you can explain it.

**Time:** O(n log n) — sort dominates. **Space:** O(1).

**Interviewer take:**
- Correct on an independent attempt from a broken first try is exactly the trajectory interviewers want to see.
- If they follow up with "can you do O(n)?" — that's when the set trick comes in. You'd want to know that answer.

---

### `submission-2.py` — O(n) set solution, looked up

```python
numSet = set(nums)
longest = 0
for num in numSet:
    if (num - 1) not in numSet:
        length = 1
        while num + length in numSet:
            length += 1
        longest = max(length, longest)
return longest
```

Correct and optimal. The key insight: only start counting a sequence when `num - 1` is not in the set — meaning `num` is the start of a sequence. This prevents counting every element as a potential start, which would give O(n²). By only starting at sequence beginnings, each element is visited at most twice (once in the outer loop, once in the inner while), giving O(n) overall.

**Time:** O(n) — set lookups are O(1), each element visited at most twice. **Space:** O(n) — the set.

---

## The textbook version

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if num - 1 not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
```

**Why it works:** Build a set for O(1) lookup. For every number that is a *sequence start* (no predecessor in the set), walk forward counting consecutive members. Because you skip non-starts, you never recount.

**Why sort-based breaks the O(n) requirement:** Sorting is O(n log n) — the problem explicitly asks for O(n). In an interview, presenting the sort solution is fine as a stepping stone, but you need to know why it's suboptimal and how to get to O(n).

**Wrong instinct this problem punishes:** Counting every element as a potential start. On `[1, 2, 3]`, starting from 1, 2, and 3 each runs 3, 2, 1 inner iterations — O(n²). The start-check is what makes it O(n).

**Time:** O(n). **Space:** O(n).

---

## Style fixes (apply going forward)

- **`else: continue` in a for loop** — `continue` after an `else` branch in a for loop is a no-op; remove it.
- **Empty check before accessing `nums[0]`** — sub-1 got this right with `if not nums: return 0`; sub-0 would crash on empty input.

---

## The pattern + where else it shows up

This is **hashing for O(1) membership testing** — the same instinct as `duplicate-integer` and `two-integer-sum`, but applied to a sequence detection problem. The set replaces the sort and turns an O(n log n) solution into O(n).

Where else it shows up in NC150:
- **Contains Duplicate** — same "have I seen this?" via set
- **Two Sum** — complement lookup via dict
- **Valid Sudoku** — membership testing across rows/cols/boxes

---

## Interview check

- Can you explain in one sentence why checking `num - 1 not in numSet` makes this O(n) instead of O(n²)?
- Did you present the sort-based solution first and then optimize? That's a clean interview narrative: brute force → sort → O(n) set.

---

## Question for you

Sub-1 iterates `numSet` (the set) in the outer loop rather than `nums` (the list). Does that matter for correctness? Would iterating `nums` instead give a different result — and if so, would it still be O(n)?

---

## Your turn — fill this in

*(Pre-filled from your submission comments — finish the rest in your own words.)*

**What I tried first:** Sort + linear scan (sub-0). Broke because the streak never reset between sequences.

**Where I got stuck:** Getting the duplicate-skip and streak-reset logic right at the same time (sub-1 solved both, but the nested while loop structure is complex).

**What made it click:** *(your words — was it seeing why `num - 1 not in numSet` avoids O(n²)? understanding that iterating the set already deduplicates? something else?)*

**Revisit?** [ ] Mark for redo in 1 week
