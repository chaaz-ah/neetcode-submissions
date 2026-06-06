# Three Integer Sum — Coach Notes

> **Heads-up before we start:** "What made it click" is still blank across `is-palindrome`, `longest-consecutive-sequence`, `valid-sudoku`, and `two-integer-sum-ii`. The pre-fills are seeds — the click moment is the part that compounds. Also: the `while s < e` vs `while s <= e` question from `two-integer-sum-ii` is unanswered. Carry both forward.

- **Problem:** https://leetcode.com/problems/3sum/
- **Pattern:** Two Pointers (after sort)
- **Difficulty:** Medium
- **Submissions:** 7 (Python)

## Verdict
Seven submissions tells the whole story: you tried to leap straight to two-pointer in sub-0/1 without the prerequisites (sort, outer loop, return-all-not-first-match), retreated to a broken O(n³) brute force in sub-2/3, landed on a working O(n³) set-of-tuples in sub-4/5, then copied NeetCode's canonical O(n²) for sub-6. The shape of the algorithm is now on the page, but two comments in sub-6 — "dont get lines 6-7" and "dont get why we do the following" — say the dedup mechanism (the whole reason this is harder than two-sum-ii) hasn't landed yet. That's the thing to fix this week.

## Submission-by-submission
### `submission-0.py` — two-pointer shape with no loop, no sort, and the wrong variable used as a value
```python
for i, first_num in enumerate(nums):
    s = i+1
    e = len(nums)-1
    partial_sum = nums[s] + nums[e]
    if partial_sum + i > 0:
        e -= 1
    ...
return [[]]
```
- `partial_sum + i` adds the **index** `i`, not `nums[i]` — same class of bug as `two-integer-sum-ii` sub-0 ("iterate values, use them as indices"). It's the second time this exact bug has shown up.
- No inner `while s < e` loop, so `s` and `e` get adjusted once and then thrown away on the next outer iteration. The two-pointer scan never actually happens.
- `nums` is never sorted, so the two-pointer move-direction logic is meaningless.
- Returns on first match (`return [...]`) and falls through to `return [[]]` (a list containing an empty list, not an empty list).
- **Time:** O(n) as written. **Space:** O(1). Both are wrong because the algorithm is wrong.

**Interviewer take:**
- The index-as-value bug repeating from `two-integer-sum-ii` would get flagged immediately — interviewer assumes you don't sanity-check on a trivial example.
- Skipping the sort means you're pattern-matching shapes, not reasoning about why two-pointer works (sorted = monotonic = directional moves are valid).

### `submission-1.py` — adds the inner loop, still no sort, still `+ i` instead of `+ nums[i]`
```python
for i in range(len(nums)-2):
    s = i+1
    e = len(nums)-1
    while s < e:
        partial_sum = nums[s] + nums[e]
        if partial_sum + i > 0:
            ...
return [[]] #bruh idk lwk forgot ts wasnt sorted
```
- The comment "lwk forgot ts wasnt sorted" is the right diagnosis — own that, it's a real catch.
- The `+ i` bug is still here. Same fix as sub-0: `partial_sum + nums[i]`.
- Still returns on first hit instead of accumulating all triplets into a `result` list.
- `range(len(nums)-2)` is fine but `enumerate(nums)` from sub-6 reads cleaner — it's also the open style debt.
- **Time:** O(n²) once the sort is in. **Space:** O(1) extra.

**Interviewer take:**
- Self-catching the missing sort in the comment is the kind of mid-solve narration that scores points — but you have to say it out loud, not just write it after.
- Returning on the first triplet is the bigger red flag than the bugs: it shows you haven't re-read the problem statement (find **all** unique triplets).

### `submission-2.py` — brute O(n³) with a broken dedup attempt
```python
for i in range(len(nums)):
    for j in range(len(nums)):
        for k in range(len(nums)):
            if (nums[i] + nums[j] + nums[k] == 0) and ((nums[i] != nums[j]) and ...):
                s = [nums[i], nums[j], nums[k]]; s.sort()
                if s not in result: result.append(s)
return result #bruh why doesnt this work
```
- `i`, `j`, `k` range over the whole array with no `j > i`, `k > j` constraint — same triple gets visited 6 times (every permutation).
- The pairwise inequality check `nums[i] != nums[j]` **excludes valid answers like `[0,0,0]`**. That's why "this doesn't work" — the bug is in the dedup heuristic, not the loop.
- `s not in result` is an O(k) scan per insert → makes the dedup step O(n³ × k). Using a `set` of tuples (what sub-3 does) is the fix.
- **Time:** O(n³) loops + O(k) per-insert check ≈ O(n³ + n³·k). **Space:** O(k).

**Interviewer take:**
- The instinct to dedup by checking pairwise inequality is the bug interviewers love to fish for — they'll hand you `[0,0,0]` as a test case and watch you discover it.
- `if s not in result` on a list is the same O(n) lookup mistake as `if x in seen_list`. Reach for a set the moment you write "have I seen this before."

### `submission-3.py` — O(n³) with sort + set + tuple, the textbook brute force
```python
result = set()
nums.sort()
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            if nums[i] + nums[j] + nums[k] == 0:
                result.add(tuple([nums[i], nums[j], nums[k]]))
return list(result) #bruh looked solution a little also forgot like set vs list like the append vs add
```
- Correct and clean for O(n³). `j > i` and `k > j` constraints kill the permutation-duplication problem from sub-2 without needing the broken pairwise check.
- Sort + tuple-into-set = canonical-form dedup. That `tuple()` trick already lives in `SYNTAX.md` from `anagram-groups` — recognizing it here is reuse, that's good.
- `set.add` vs `list.append` is worth committing: lists use `append`, sets use `add`, dicts use `[k] = v`. If you mix them up in an interview, the linter won't save you.
- **Time:** O(n³). **Space:** O(k) for unique triplets.

**Interviewer take:**
- Correct brute force after stating the approach is fine — most candidates start here, then optimize. The problem is you didn't say "this is O(n³), I think we can do O(n²) by exploiting the sort" before writing it.

### `submission-4.py` — same O(n³), cleaner one-liner return
```python
return [list(i) for i in res]
```
- Identical to sub-3 except for the return. The list comprehension is the idiomatic way to convert `set[tuple]` → `list[list]`.
- Worth keeping in muscle memory: `[list(t) for t in some_set_of_tuples]`.

### `submission-5.py` — byte-for-byte duplicate of sub-4
```python
# (identical to sub-4)
```
- Zero new information. Probably a re-run, not a re-attempt. Skip.

### `submission-6.py` — the canonical O(n²) two-pointer, but the dedup machinery isn't internalized
```python
for i, a in enumerate(nums):
    if i > 0 and a == nums[i -1]:
        continue
    #also dont get lines 6-7
    s, e = i + 1, len(nums)-1
    while s < e:
        twoSum = nums[s] + nums[e] + a
        if twoSum > 0: e -= 1
        elif twoSum < 0: s += 1
        else:
            result.append([a, nums[s], nums[e]])
            #i dont get why we do the following like lines21-24 for
            s += 1; e -= 1
            while nums[s] == nums[s-1] and s < e:
                s += 1
```
- The algorithm is right. Two issues to chew on:
  1. **Outer skip (`if i > 0 and a == nums[i-1]: continue`)** — this is "skip this `i` if it produces the same triplet family I already explored." Example: `nums = [-1,-1,0,1,2]`. With `i=0` you find `[-1,-1,2]` and `[-1,0,1]`. With `i=1` (same value `-1`), the inner two-pointer would find the same triplets again. The skip prevents that. The `i > 0` guard is just so you don't index `nums[-1]` on the first iteration.
  2. **Inner skip after a match** — once you've recorded `[a, nums[s], nums[e]]`, the next `s` could be the same value (e.g., `nums = [-2,0,0,0,2]`, after the first `[-2,0,2]` you don't want to record it again). The `while nums[s] == nums[s-1] and s < e: s += 1` advances past the duplicates of the **left** pointer. Note: you're only deduping `s`, not `e`. The standard solution adds a symmetric `while nums[e] == nums[e+1] and s < e: e -= 1` after `e -= 1`. Yours still produces correct answers because once you advance `s` past duplicates and the next iteration computes `twoSum` again, mismatches will be filtered — but it does extra work.
  3. **Short-circuit ordering nit:** `while nums[s] == nums[s-1] and s < e` evaluates `nums[s]` first. If `s` ever reached `len(nums)`, that's an IndexError. It can't here because `s < e` from the outer guard and `e < len(nums)`, but stylistically the `s < e` check should go first: `while s < e and nums[s] == nums[s-1]`.
- **Time:** O(n²) — outer loop O(n), inner two-pointer O(n) per outer. Sort is O(n log n), dominated. **Space:** O(1) extra (output not counted).

**Interviewer take:**
- An interviewer would ask "why the `if i > 0 and a == nums[i-1]: continue`?" — your written comment says you don't know. If that comes out of your mouth in a loop, you're done. Internalize **before** the interview.
- Stating "I'll sort first so I can move pointers monotonically, then I need two layers of dedup — one for `i`, one inside the two-pointer when I record a match" is the kind of upfront framing that buys you grace if the implementation stumbles.

## The textbook version
```python
def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    for i, a in enumerate(nums):
        if a > 0:
            break                          # sorted: no triple summing to 0 once we're past 0
        if i > 0 and a == nums[i - 1]:
            continue                       # outer dedup
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = a + nums[l] + nums[r]
            if s > 0:
                r -= 1
            elif s < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1               # inner dedup for left
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1               # inner dedup for right (yours is missing this)
    return res
```
**Why it works:** Sorting turns "find triplets summing to 0" into "fix one element, two-sum the rest with two pointers." Sort enables both: (1) monotonic pointer moves and (2) cheap dedup by skipping equal neighbors. The `if a > 0: break` is a free early exit since the smallest of any triple from here would already be positive.

**Wrong instincts this problem punishes:**
- Pairwise inequality as dedup (sub-2) — wrongly excludes `[0,0,0]`.
- Hashmap two-sum nested inside an outer loop — works but dedup gets messy because you don't have ordering to lean on.
- Returning early on the first match (sub-0/1) — "find all" is in the problem statement.

**Time:** O(n²). **Space:** O(1) extra, O(k) for output.

## Style fixes (apply going forward)
- `range(len(nums))` in sub-1/2/3/4/5 — use `enumerate(nums)` when you need both. Sub-6 already does this, so it's not a knowledge gap, it's habit.
- `return [[]]` (sub-0/1) vs `return []` — `[[]]` is a list containing one empty list, which is a wrong answer; `[]` is "no triplets found." Read the type signature.
- Variable names: `s` and `e` for left/right pointers is fine, but `l` and `r` (left/right) is the convention you'll see in every solution.

## The pattern + where else it shows up
**Pattern:** Sort → fix one element → two-pointer the rest, with explicit dedup at both layers.

Same instinct shows up in:
- **`two-integer-sum-ii`** — the inner two-pointer half of this problem. You did it independently in sub-2 there; sub-6 here is the same loop, just nested.
- **3Sum Closest / 4Sum** — NC150 successors. Once you own the dedup mechanics, those are direct extensions (4Sum = one more outer loop).
- **Container With Most Water** (which you just submitted) — different decision rule (move the smaller height instead of the smaller sum), same two-pointer scaffolding.

## Interview check
- Did you state O(n²) upfront and contrast with O(n³) brute force?
- Could you explain the outer skip and the inner skip without a comment that says "dont get"?
- Did you handle `[0,0,0]` as a deliberate test case, not as a bug you stumbled into?

## Question for you
The inner dedup loop is `while nums[s] == nums[s-1] and s < e: s += 1`. **Why does this advance `s` past duplicates instead of advancing it just once?** Walk through `nums = [-2, 0, 0, 0, 2]` with `i = 0` (a = -2) — how many times does the inner skip-loop fire, and what triplets would you produce if you removed the loop and only did `s += 1` once?

## Your turn — fill this in

*(Pre-filled from your submission comments — fill in the rest yourself. The "What made it click" line is the one that matters.)*

**What I tried first:** Two-pointer shape from `two-integer-sum-ii` without sorting or an inner loop (sub-0/1) — same index-as-value bug as last time. Retreated to brute force (sub-2/3/4/5), landed on a `set` of `tuple`s for dedup.

**Where I got stuck:** Two places, explicit in your comments on sub-6: the outer skip `if i > 0 and a == nums[i-1]: continue` (lines 6-7) and the inner skip-loop after a match (lines 21-24). The mechanism of dedup is the gap.

**What made it click:** *(your words — was it tracing `[-1,-1,0,1,2]` by hand? seeing that sort makes "have I seen this triplet" a neighbor-equality check? something else? write it here.)*

**Revisit?** [ ] Mark for redo in 1 week
