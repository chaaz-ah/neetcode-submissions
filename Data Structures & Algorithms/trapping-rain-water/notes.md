# Trapping Rain Water — Coach Notes

- **Problem:** https://leetcode.com/problems/trapping-rain-water/
- **Pattern:** Prefix-Suffix Max Arrays / Two Pointers (O(1) space)
- **Difficulty:** Hard
- **Submissions:** 4 (Python)

---

> ⚠️ **Carry-forward flag:** The max-water-container "Question for you" is still unanswered. It was: *Why does moving the larger pointer never help? Construct a small example.* The "What made it click" section is also blank. Same issue in three-integer-sum. Blank reflection sections are the pattern that's going to slow you down — the review is only half the learning.

---

## Verdict

Sub-0 misread the problem — uses immediate neighbors instead of global maxima, and accumulates max instead of sum. Sub-1 got the structure right (prefix/suffix arrays) after watching a video but has six distinct bugs, including `for i in water: sum += water[i]` — iterating values and using them as indices, now appearing for the **third time** across this repo. Subs 2 and 3 are both correct looked-up solutions: O(n) prefix/suffix and O(1) two-pointer. Worth noting: sub-1 used `for i, value in enumerate(height)` correctly in the left pass — that's the `range(len())` pattern finally showing up less.

## Submission-by-submission

### `submission-0.py` — wrong mental model: immediate neighbors, not global maxima

```python
for i in range(1, len(height)-1):
    l = i-1
    r = i+1
    water = min(height[l], height[r]) - height[i]
    maxWater = max(water, maxWater)
return maxWater
#bruh idk
```

- **Core misread:** `min(height[l], height[r])` checks the immediate neighbors, not the max height across the entire left or right side. Water at position `i` is bounded by the tallest wall anywhere to the left and the tallest wall anywhere to the right — a taller bar three steps away still constrains how high water can rise. Checking `i-1` and `i+1` only works in the degenerate case where the tallest walls happen to be adjacent.
- **Wrong accumulation:** `max(water, maxWater)` returns the *maximum* water at any single cell, not the *sum* across all cells. This problem asks for total trapped water — you need `res += max(water, 0)` in a loop, not `max(...)` outside one.
- Dead code: `while height[s] != 0: s += 1` at the top — `s` is computed and never referenced again.
- **Time:** O(n). **Space:** O(1). Output is wrong regardless.

**Interviewer take:**

- Before touching the keyboard, pin down the formula: "water at `i` = min(max height to the left, max height to the right) − height[i]." One sentence. Writing code without this stated out loud signals you're coding from feel rather than a model — an interviewer will stop you and ask.
- "bruh idk" is honest, but in an interview you'd want to say "let me think through what the water at each cell actually depends on" before committing to a direction. That pause is free.

### `submission-1.py` — right structure, six bugs, including the recurring index-as-value error

```python
maxLeft = [] * len(height)   # BUG 1: [] * N is always []
...
for i, value in enumerate(height):
    if value > left:
        left = value
    maxLeft[i] = value        # BUG 2: should be `left` (running max), not `value` (current element)

for i in range(len(height), 0, -1):   # BUG 3: starts at OOB index len(height)
    if value > right:                  # BUG 4: `value` is stale from the enumerate loop above
        right = value
    maxRight[i] = value               # BUG 5: should be `right`
...
for i in water:
    sum += water[i]   # BUG 6: iterates VALUES, uses them as indices — third appearance of this bug
#watched the video but still idk
```

- **Bug 1:** `[] * len(height)` evaluates to `[]` — multiplying an empty list by any number is still an empty list. You want `[0] * len(height)`.
- **Bug 2:** `maxLeft[i] = value` stores the current element, not the running max. `left` is the variable tracking the running max — that's what belongs in the array. `max(left, value)` is also fine and arguably clearer.
- **Bug 3:** `range(len(height), 0, -1)` starts at index `len(height)` which is out of bounds. The right-pass range is `range(n-2, -1, -1)` (second-to-last down to zero), with the last element seeded beforehand as `rightMax[n-1] = height[n-1]`.
- **Bug 4 & 5:** `value` is the loop variable from `enumerate(height)` above. After that loop ends, it holds the last element of `height` — a stale borrow. Inside the second loop, use `height[i]` for the current element and `right` for the running max.
- **Bug 6:** `for i in water: sum += water[i]` — `i` iterates over the *values* in `water`, then those values get used as indices into `water`. This is the exact bug from `two-integer-sum-ii` sub-0. Third appearance. The fix: `return sum(water)`, or `for w in water: total += w`.
- Also: `sum` shadows the builtin — use `total` or `res`.
- One genuine win: `for i, value in enumerate(height)` in the left pass — that's correct use of `enumerate`. Worth noting since `range(len())` has been a recurring flag.
- **Time/Space with bugs fixed:** O(n) / O(n). As written, crashes on the first list append.

**Interviewer take:**

- Six bugs after watching a video signals the mental model isn't there yet — structure was borrowed but semantics weren't. An interviewer would ask "walk me through what `maxLeft[i]` should hold" before you write anything. Answer: "the maximum height from index 0 through i, inclusive." That sentence pins the algorithm.
- The `for i in water: sum += water[i]` error — if this appears in an interview, the interviewer catches it immediately. Fix the pattern now: iterating over a list gives you *values*; if you need indices, use `enumerate` or `range(len())`.

### `submission-2.py` — correct O(n) prefix/suffix max solution

```python
leftMax[0] = height[0]
for i in range(1, n):
    leftMax[i] = max(leftMax[i - 1], height[i])

rightMax[n - 1] = height[n - 1]
for i in range(n - 2, -1, -1):
    rightMax[i] = max(rightMax[i + 1], height[i])

res = 0
for i in range(n):
    res += min(leftMax[i], rightMax[i]) - height[i]
return res
#based on other vids, this is prob most reasonable sol to solve in interview still ts is so hard
```

- Correct and clean. Seeds each end, propagates the running max inward on both sides, then one pass to accumulate water.
- `min(leftMax[i], rightMax[i]) - height[i]` is always ≥ 0 because both arrays include `height[i]` in their max — no `max(..., 0)` guard needed.
- "ts is so hard" — this is a Hard problem. Looking up the prefix/suffix approach after two broken genuine attempts is the right call. Knowing *why* the formula works is the remaining gap to close.
- **Time:** O(n) — three linear passes. **Space:** O(n) — two arrays of size n.

### `submission-3.py` — correct O(1) space two-pointer

```python
l, r = 0, len(height) - 1
leftMax, rightMax = height[l], height[r]
res = 0
while l < r:
    if leftMax < rightMax:
        l += 1
        leftMax = max(leftMax, height[l])
        res += leftMax - height[l]
    else:
        r -= 1
        rightMax = max(rightMax, height[r])
        res += rightMax - height[r]
return res
#ts hard asf
```

- Correct. The order inside each branch matters: advance pointer first, update max second, accumulate third. If you updated `leftMax` before advancing `l`, you'd use the old position's height.
- The insight that makes this work: when `leftMax < rightMax`, the water at `l` is bounded by `leftMax` regardless of what's to the right — something ≥ `leftMax` exists at `r` or beyond. So `leftMax` is the tight constraint, and you can accumulate `leftMax - height[l]` confidently before looking right.
- Same "move the bottleneck side" rule as max-water-container, but here you accumulate water at each step instead of just tracking a max area.
- **Time:** O(n). **Space:** O(1).

## The textbook version

Sub-2 *is* the textbook version for most interview contexts — O(n) time, O(n) space, straightforward to derive. Sub-3 is the space-optimized follow-up.

**Core formula:**
```
water[i] = min(max(height[0..i]), max(height[i..n-1])) - height[i]
```
Precompute both maxima in two passes to avoid recomputing them for each cell.

```python
def trap(self, height: List[int]) -> int:
    n = len(height)
    leftMax, rightMax = [0] * n, [0] * n
    leftMax[0] = height[0]
    for i in range(1, n):
        leftMax[i] = max(leftMax[i - 1], height[i])
    rightMax[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        rightMax[i] = max(rightMax[i + 1], height[i])
    return sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
```

**Why the two-pointer works (sub-3 shape):** When `leftMax < rightMax`, the water at `l` is entirely determined by `leftMax` — there's guaranteed something taller on the right, so the left side is the bottleneck. Move `l`, update `leftMax`, accumulate. Mirror on the right side. This is the max-water-container "move the smaller" rule applied to accumulation.

**Wrong instincts this problem punishes:**
- Checking immediate neighbors (sub-0) — water is bounded by *global* left and right maxima, not adjacent cells.
- Storing `value` (current element) instead of `left` (running max) in the prefix array — the whole point of the array is to capture the cumulative max, not re-record the input.
- `for i in collection: use collection[i]` — gives you a value, not an index.

**Time:** O(n). **Space:** O(n) prefix/suffix, O(1) two-pointer.

## Style fixes (apply going forward)

- **`[0] * n` for list initialization** — `[] * n` is always `[]`. This one will crash immediately in any test; add it to muscle memory.
- **`for i in collection: use collection[i]`** is the third appearance of this pattern — iterating values and using them as indices. Write `sum(collection)`, `for val in collection: total += val`, or `for i, val in enumerate(collection)` depending on what you need.
- **Don't shadow `sum`** — use `total` or `res`.
- **Stale loop variables** — `value` from `for i, value in enumerate(height)` is still in scope after the loop. Don't reuse it in a second loop; name a fresh variable (`cur`, `h`, or just index directly with `height[i]`).

## The pattern + where else it shows up

**Pattern:** Prefix-suffix decomposition — precompute a left-side aggregate and a right-side aggregate so each cell can answer "what's the best value on my left / right?" in O(1).

- **`products-of-array-discluding-self`** — same shape exactly. `prefix[i]` = product of all elements to the left of i; `suffix[i]` = product of all elements to the right. The formula is different but the two-pass structure is identical.
- **max-water-container two-pointer** — same "move the bottleneck side" rule as sub-3 here. The extra bookkeeping is that you accumulate water at each step rather than just tracking a max.

## Question for you

Sub-1's `maxLeft[i] = value` stores the current height instead of the running max. In your own words: what should `leftMax[i]` actually hold, and why does `max(leftMax[i-1], height[i])` give you that? If you can explain this without looking at the code, you own the prefix-max pattern — and you'll recognize it immediately when `products-of-array-discluding-self` shows up again.

## Your turn — fill this in

*(Pre-filled from your submission comments — fill in the rest yourself.)*

**What I tried first:** Immediate-neighbor approach (sub-0) — "bruh idk." Tried prefix/suffix arrays after watching a video (sub-1) — "still idk" even with the structure.

**Where I got stuck:** Sub-1 — six bugs despite having the right shape. The list initialization (`[] * n`), the stale `value` variable in the right pass, and the index-as-value error at the end.

**What made it click:** *(your words)*

**Revisit?** [ ] Mark for redo in 1 week
