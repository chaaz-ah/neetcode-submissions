# Container With Most Water — Coach Notes

- **Problem:** https://leetcode.com/problems/container-with-most-water/
- **Pattern:** Two Pointers (greedy inward scan)
- **Difficulty:** Medium
- **Submissions:** 3 (Python)

## Verdict
Clean progression: independent O(n²) brute force in sub-0, an honest two-pointer attempt in sub-1 with two real bugs (width sign, movement inside `else`), and a correct O(n) two-pointer in sub-2 with the bugs fixed after a hint. The comment on sub-2 — "the hint that you should move the larger height was monumental" — is worth pausing on, because it's actually backwards. The rule is **move the smaller height**, not the larger. Your code does the right thing; your stated rule contradicts it. Fix the verbal rule before the interview, otherwise you'll write the code right and explain it wrong.

## Submission-by-submission
### `submission-0.py` — independent O(n²) brute force, correct
```python
highArea = 0
for i in range(len(heights)-1):
    for j in range(i+1, len(heights)):
        area = (min(heights[i], heights[j])) * (j-i)
        if area > highArea:
            highArea = area
return highArea
#did this on my own lol
```
- Correct. Width `(j-i)` is right, `min(heights[i], heights[j])` is right, `j > i` constraint is right. No off-by-one.
- `highArea = max(highArea, area)` is one line shorter than the `if area > highArea: highArea = area` — same logic, cleaner read.
- "did this on my own lol" — log this. After the rough start on `three-integer-sum`, an independent brute force on a new Two Pointers problem is a real signal.
- Style: `range(len(...))` for both loops where you only need `i` and `j` as indices — fine here since you don't have a single iterable to enumerate.
- **Time:** O(n²) — every pair. **Space:** O(1).

**Interviewer take:**
- A clean brute force stated out loud as "let me start with the O(n²) so we're aligned on what we're optimizing" is exactly what you want as a warm-up — buys you grace and credit before you reach for the trick.

### `submission-1.py` — two-pointer attempt with width sign bug and movement-in-`else` bug
```python
s = 0
e = len(heights)-1
minArea = 0
while s < e:
    if min(heights[s], heights[e]) * (s-e) > minArea:
        minArea = min(heights[s], heights[e]) * (s-e)
    else:
        if heights[s] > heights[e]:
            e -= 1
        if heights[s] < heights[e]:
            s += 1
return minArea
#alr this is what i thought of ig
```
- **Bug 1 — width is negated:** `(s-e)` is always negative (`s < e`). `min(...) * negative` is ≤ 0, never beats `minArea = 0`, so the `if` branch never fires. You always go into `else`.
- **Bug 2 — pointers only move in `else`:** Even with the width fixed, advancing pointers only when the new area *didn't* improve means the moment you hit a better area, both pointers freeze and you loop forever.
- **Bug 3 — ties stall:** When `heights[s] == heights[e]`, neither `if` fires inside `else` — infinite loop on equal heights.
- **Name:** `minArea` while tracking a *max* — variable name lies about intent. Same class of issue as `count` for a sum.
- **Movement direction itself is correct** (`if heights[s] > heights[e]: e -= 1` moves the smaller pointer inward), but it's stuck inside `else` so it doesn't always run.
- **Time / Space:** With infinite-loop bugs, complexity is undefined. If patched: O(n) / O(1).

**Interviewer take:**
- The "always go into `else`" trap from a sign bug is the kind of thing dry-running on `[1,2]` catches in 10 seconds. Walking through one example by hand before claiming you're done is the cheapest debug there is.
- Pointer-movement-as-side-effect-of-the-update is a structural smell. Movement should be unconditional each iteration, area update separate.

### `submission-2.py` — correct two-pointer, comment exposes a backward mental model
```python
s = 0
e = len(heights)-1
minArea = 0
while s < e:
    area = min(heights[s], heights[e]) * (e-s)
    minArea = max(area, minArea)

    if heights[s] > heights[e]:
        e -= 1
    elif heights[s] < heights[e]:
        s += 1
    else:
        e -= 1
return minArea
#broooo omg i almost got it i did s-e instead of e-s but kinda saw some hints and vid and also the hint that you should move the larger height was monumental
```
- Correct. Width fixed (`e-s`), area + max in two clean lines, movement unconditional, tie-break handled (`else: e -= 1` is arbitrary — `s += 1` works equally well).
- `if heights[s] > heights[e]: e -= 1` — when `heights[s] > heights[e]`, the *smaller* side is `heights[e]`, so you move `e`. That's "move the **smaller** pointer." Your comment says "move the **larger** height was monumental" — that's the opposite of what your code does. Two possible reads:
  - You meant "the pointer at the smaller height" but wrote "larger" — fine, just fix the wording.
  - You actually internalized it backward and the code happens to be right because the condition flips the right way — risky, because under interview stress you'll explain it backward, then doubt the code.
- **Why move the smaller?** The smaller height is the *limiting* factor. Moving the larger pointer can never increase area (width shrinks, height capped by the same smaller side). Moving the smaller pointer is the only move with upside — you trade width for a chance at a taller minimum.
- `minArea` still misnamed.
- **Time:** O(n) — each pointer moves inward, total moves ≤ n. **Space:** O(1).

**Interviewer take:**
- An interviewer would ask "why move the smaller side?" — if you answer "move the larger," they'll stop and re-test your understanding. Get the verbal rule right.
- "I almost had it, fixed s-e to e-s after a hint, then the movement rule clicked" is fine to say honestly — better than pretending you knew it cold.

## The textbook version
```python
def maxArea(self, heights: List[int]) -> int:
    l, r = 0, len(heights) - 1
    best = 0
    while l < r:
        best = max(best, min(heights[l], heights[r]) * (r - l))
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
    return best
```
**Why it works:** Start with the widest possible container. At each step, the **smaller** side is the limit on area — moving it is the only move that *could* improve. Moving the larger side can't help: the new width is smaller, and the height is still capped by the unchanged smaller side. So a greedy "move the smaller pointer inward" sweeps through all containers that could plausibly be optimal in O(n).

**Wrong instincts this problem punishes:**
- Trying all pairs (sub-0 brute force) — works, but O(n²); interviewer expects you to get to O(n).
- Moving the *larger* pointer or the one that just decreased — both miss the optimum.
- Sliding window with a window-size constraint — there's no window size; this is two-pointer-as-search, not as-window.

**Time:** O(n). **Space:** O(1).

## Style fixes (apply going forward)
- **Variable naming lies:** `minArea` for a running *max* — rename to `best`, `max_area`, or `highArea` (which you used in sub-0 correctly).
- **Movement should be unconditional in two-pointer.** If movement only happens in one branch of `if/else`, you almost certainly have an infinite-loop bug. Compute area → update best → move. Three lines, no nesting.
- **Dry-run one example by hand before submitting.** The `(s-e)` sign bug dies on `[1,1]` in five seconds.
- `range(len(...))` showed up in sub-0 — acceptable when you need two indices, but reach for `enumerate` when you have a value+index pair (carries over from open style debts).

## The pattern + where else it shows up
**Pattern:** Two Pointers — greedy inward scan with a movement rule based on which side is the bottleneck.

Where else you'll see this exact shape:
- **`trapping-rain-water`** (next NC150 in the section) — same "move the smaller side" rule, harder bookkeeping (track max heights seen on each side).
- **`is-palindrome` / `two-integer-sum-ii`** — same scaffolding (l/r pointers, `while l < r`), different decision rule (compare chars, compare sum to target).
- **`three-integer-sum` sub-6** — nests this exact loop inside an outer iteration.

The Two Pointers pattern is now three problems deep — that's enough to start naming it out loud before you start coding.

## Interview check
- Did you state the brute force first and call out O(n²) → O(n) as the optimization target?
- Can you explain *why* you move the smaller pointer (not just *that* you do)?
- Did you justify O(1) space without being asked?

## Question for you
Why does moving the **larger** pointer never help? Construct (or sketch) a small example where moving the larger side gives a strictly worse next-area and convince yourself there's no case where it could win. If you can articulate this without hand-waving, you own this problem.

## Your turn — fill this in

*(Pre-filled from your submission comments — fill in the rest yourself.)*

**What I tried first:** Brute force O(n²) — nested pair loop, independent (sub-0 "did this on my own lol").

**Where I got stuck:** Two-pointer in sub-1 — wrote `(s-e)` instead of `(e-s)`, and put pointer movement inside the `else` branch so it never fired when the area improved.

**What made it click:** *(your words — also reconcile this: your comment says "move the larger height," but your code moves the smaller. Which one did you actually mean, and why?)*

**Revisit?** [ ] Mark for redo in 1 week
