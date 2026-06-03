# Two Integer Sum II — Coach Notes

- **Problem:** https://neetcode.io/problems/two-integer-sum-ii
- **Pattern:** Two Pointers
- **Difficulty:** Medium
- **Submissions:** 3 (Python)

> **Before we start:** The "What made it click" in your valid-sudoku "Your turn" is still blank. That's the one thing the whole reflection is built around — go fill it in before moving on.

---

## Verdict

Sub-0 has a fundamental indexing bug that would crash or return wrong results. Sub-1 patches it correctly but stays O(n²) — brute force on a sorted array, which ignores the structure entirely. Sub-2 is the right solution, implemented independently after watching the algorithm walk-through. The two-pointer click happened, which is real — the comment shows genuine ownership of the implementation.

---

## Submission-by-submission

### `submission-0.py` — wrong: iterates values, uses them as indices

```python
for i in numbers:
    for j in numbers:
        if numbers[i] + numbers[j] == target:
            return [i+1, j+1]
```

- `i` here is a **value** from `numbers`, not an index. `numbers[i]` uses that value as an index — on a list like `[2, 7, 11, 15]`, `i = 2` gives `numbers[2] = 11`, not the element `2`. Wrong behavior, would crash on any input where a value exceeds the list length.
- Even if the indexing were right, this is O(n²) nested loop — doesn't use the sorted property at all.
- Return `[i+1, j+1]` also wrong because `i` and `j` are values, not indices.

**Time:** O(n²) · **Space:** O(1)

**Interviewer take:**
- The `for i in numbers` / `numbers[i]` pattern is a classic "iterating values, treating them as indices" bug. Interviewers test for exactly this — they'd ask "walk me through what `i` is here" and wait for you to catch it yourself.
- No use of the sorted constraint is an immediate flag: problem says the array is sorted — if you're not using that, you're missing the whole point.

---

### `submission-1.py` — correct indexing, still brute force

```python
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i] + numbers[j] == target:
            return [i+1, j+1]
```

- Indexing is now correct — `range(len(numbers))` gives actual indices. Good fix.
- Still O(n²). The sorted constraint is still being completely ignored.
- Also: when `i == j`, you're checking if `2 * numbers[i] == target`, which is wrong for "indices must be different." The problem guarantees exactly one solution with distinct indices, but this doesn't enforce it.

**Time:** O(n²) · **Space:** O(1)

**Interviewer take:**
- `range(len(numbers))` — no enumeration needed here since you're not using the value alongside the index, but this is the same `range(len())` habit. Not a blocker, but noted.
- Brute force on a sorted array signals you haven't identified the useful property. Interviewers expect you to say "it's sorted, so I can use two pointers or binary search" before writing O(n²).

---

### `submission-2.py` — correct two-pointer solution

```python
s = 0
e = len(numbers)-1

while s < e:
    if numbers[s] + numbers[e] > target:
        e -= 1
    if numbers[s] + numbers[e] < target:
        s += 1
    if numbers[s] + numbers[e] == target:
        return [s+1, e+1]
return []
```

- Correct logic, correct result. The two-pointer intuition is right: sum too big → move right pointer in, sum too small → move left pointer out.
- One subtle bug: the three `if` branches aren't `elif`. After `e -= 1`, you re-evaluate `numbers[s] + numbers[e]` in the next `if`. In practice this doesn't cause wrong answers (the loop still terminates correctly), but it does one extra comparison per decrement. Use `elif` to make it explicit and slightly cleaner.
- `s = 0`, `e = len(numbers)-1` — clean names for two-pointer. `lo`/`hi` or `left`/`right` are conventional, but `s`/`e` reads fine.

**Time:** O(n) — single pass, each pointer moves at most n times · **Space:** O(1)

**Interviewer take:**
- Comment says "omg i saw the neetcode video on the process but i implemented this by myself" — that's an honest flag. The interviewer cares whether you can implement it independently given the *idea*. Watching an algorithm walk-through and then coding it is a real skill. Own it.
- The `if / if / if` vs `elif` issue: minor, but in a live interview you'd want to catch it and say "these should be elif since the conditions are mutually exclusive."

---

## The textbook version

```python
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left + 1, right + 1]
        elif s < target:
            left += 1
        else:
            right -= 1
    return []
```

**Why it works:** The array is sorted. At any point, `numbers[left]` is the smallest unused value and `numbers[right]` is the largest. If their sum is too big, the only way to decrease it is to decrease the right pointer (moving left shrinks the max). If too small, increase the left pointer. You're guaranteed to converge on the answer in O(n).

**What the wrong instinct costs:** Treating this as an unsorted Two Sum and reaching for a hashmap gives O(n) time and O(n) space — correct, but throws away the sorted constraint. Two pointers is O(n) time and O(1) space. The problem literally tells you the answer: "1-indexed sorted array."

**Time:** O(n) · **Space:** O(1)

---

## Style fixes (apply going forward)

- **`if / if / if` → `elif`** when conditions are mutually exclusive. A sum can't simultaneously be `> target` and `< target`. Three `if`s means three comparisons; `if / elif / else` is one.
- **`range(len())`** — still showing up. Not wrong here, but the habit is persistent.

---

## The pattern + where else it shows up

**Two Pointers (inward scan)** — start at both ends of a sorted structure, move inward based on a comparison. The key insight: sorted order lets you make a *guaranteed directional decision* at each step, which gets you O(n) instead of O(n²).

Other NC150 problems using the same instinct:
- **3Sum** — outer loop fixes one element, inner loop uses two pointers on the remainder
- **Container With Most Water** — maximize area, move the shorter side inward (same directional argument)
- **Trapping Rain Water** — two-pointer variant tracking left/right max

---

## Question for you

In sub-2, `while s < e` is the loop guard. What happens if you change it to `while s <= e`? Does it ever cause an infinite loop, a wrong answer, or does it not matter?

---

## Your turn — fill this in

*(Pre-filled from your submission comments — finish the rest in your own words.)*

**What I tried first:** Nested loop, iterating over values then indices — the indexing bug in sub-0, fixed to actual indices in sub-1.

**Where I got stuck:** Getting to the two-pointer idea — needed to see the algorithm walk-through before sub-2.

**What made it click:** *(your words — was it the sorted property? seeing that moving a pointer is a guaranteed direction? something else?)*

**Revisit?** [ ] Mark for redo in 1 week
