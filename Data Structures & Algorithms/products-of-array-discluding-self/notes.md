# Products of Array Discluding Self — Coach Notes

- **Problem:** https://leetcode.com/problems/product-of-array-except-self/
- **Pattern:** Arrays & Hashing / Prefix Products
- **Difficulty:** Medium
- **Submissions:** 5 (Python)

---

> **Carry-forward from string-encode-and-decode:** "What made it click" in the "Your turn" section is still blank. That part can't be pre-filled — it needs to be your words. The question there was: *what was the moment the length-prefix framing made sense — was it seeing `len#str`, understanding why the `#` is safe to scan for, or realizing you slice by position rather than search?* Fill that in. The reflection is the whole point.

---

## Verdict

Sub-0 got the brute force right with ChatGPT assist. Sub-1 shows you understood the prefix/postfix idea after watching the NeetCode video, but the implementation is broken in two different ways — the prefix/postfix arrays store individual values instead of running products, and the boundary condition has an operator precedence bug that makes it always evaluate False. Sub-2 is a retreat back to O(n²) while you were still working it out. Subs 3 and 4 are the correct O(n) NeetCode solution — clean and correct, but looked up. **Assist level: sub-0 ChatGPT assisted / sub-1 watched algorithm then independently attempted (broken) / sub-2 unclear (no comment) / sub-3/4 looked up solution.**

---

## Submission-by-submission

### `submission-0.py` — Correct brute force, ChatGPT assisted

```python
for i in range(len(nums)):
    mul = 1
    for j in range(len(nums)):
        if i == j:
            continue
        mul *= nums[j]
    otp.append(mul)
```

- Logic is correct — for each index, multiply everything except `nums[i]`. O(n²) time, O(n) space.
- `range(len(nums))` shows up twice — the outer loop doesn't need an index at all to skip `j == i`, and the inner skip logic is also clunky. Style debt still alive.
- Comment says ChatGPT helped — brute force is conceptually straightforward enough that this is fine for a first pass, but you shouldn't need assistance here.

**Interviewer take:**
- O(n²) nested loop is expected as a brute force opening — fine if you name it and say "I'll optimize." What's not fine is stopping here.
- `range(len(nums))` in both loops when the inner one doesn't use `i` except to skip it — signals habit, not intent.

---

### `submission-1.py` — Right instinct, two separate bugs that break it entirely

```python
for i in range(len(nums)):
    mul = 1
    mul *= nums[i]
    prefix.append(mul)
for i in range(len(nums)-1, 0, -1):
    mul = 1
    mul *= nums[i]
    postfix.append(mul)
for i in range(len(nums)):
    mul = 1
    if i != 0 | i != len(nums)-1:
        mul = prefix[i-1] * postfix[i+1]
    output.append(mul)
```

Two bugs, either one is fatal:

**Bug 1 — prefix/postfix arrays aren't prefix products.** The build loops reset `mul = 1` every iteration, then do `mul *= nums[i]`, so each element in `prefix` is just `nums[i]`. A running prefix product requires carrying `mul` across iterations — not resetting it.

**Bug 2 — operator precedence on the boundary check.** In Python, `|` (bitwise OR) has *higher* precedence than `!=`. So `i != 0 | i != len(nums)-1` parses as `i != (0 | i) != len(nums)-1`, which is `i != i != len(nums)-1`. Since `i != i` is always False, the entire condition is always False — `mul` is always 1, and `output` is all 1s regardless of input. The fix was `or`, not `|`.

- The right idea is here (prefix products, postfix products, multiply the two), which is real progress from sub-0.
- `range(len(nums))` debt still present — three loops, none use `enumerate`.

**Interviewer take:**
- If you caught bug 1 yourself and narrated the fix, that's actually impressive signal — "I notice my prefix isn't accumulating, let me carry the product across iterations." If you silently stared at wrong output, that's the concern.
- `|` vs `or` is a Python-specific trap. Using the wrong one here wouldn't get you flagged hard, but not catching that the condition always evaluates False would.

---

### `submission-2.py` — Back to O(n²), no comment

```python
otp = [0] * len(nums)
for i in range(len(nums)):
    mul = 1
    for j in range(len(nums)):
        if i == j:
            continue
        mul *= nums[j]
    otp[i] = mul
return otp
```

- Same logic as sub-0, minor refactor (pre-allocated array vs append). No new signal here.
- No comment — hard to know if this was "I'll fix the brute force while I figure out prefix/postfix" or just stuck.
- `range(len(nums))` debt still present.

---

### `submission-3.py` — Correct O(n), looked up

```python
prefix = 1
postfix = 1
otp = [1] * len(nums)
for i in range(len(nums)):
    otp[i] = prefix
    prefix *= nums[i]
for i in range(len(nums)-1, -1, -1):
    otp[i] *= postfix
    postfix *= nums[i]
return otp
```

- This is the canonical solution. Clean, correct, O(n) time, O(1) extra space (output array doesn't count).
- Pre-seeding `otp` with 1s is the move — lets you accumulate prefix into `otp[i]` *before* multiplying in `nums[i]`, and postfix into `otp[i]` *before* multiplying in `nums[i]` from the right.
- No style debts in this one — no builtin shadowing, no trailing semicolons.
- `range(len(nums))` appears but in both loops the index is exactly what's needed (modifying `otp[i]` by position), so `enumerate` wouldn't simplify this.

---

### `submission-4.py` — Same as sub-3, re-submit to confirm

Identical to sub-3 — looks like a re-run to verify it passed. Nothing new to flag.

---

## The textbook version

The key insight: for each index `i`, the answer is `product of everything to the left of i` × `product of everything to the right of i`. If you can compute those two independently and multiply them, you never divide and you never need O(n) extra space per position.

```python
def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix       # store left product before including nums[i]
        prefix *= nums[i]        # update running left product

    postfix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= postfix     # multiply in right product
        postfix *= nums[i]       # update running right product

    return result
```

**Why it works:** On the first pass, `result[i]` holds the product of all elements to the *left* of `i` (since we store `prefix` before folding in `nums[i]`). On the second pass, we multiply in the product of all elements to the *right* of `i` (same idea, from the right). The output is built in-place with only two scalar variables — no prefix/postfix arrays needed.

**Wrong instincts this problem punishes:**
- Building separate prefix/postfix *arrays* — not wrong, but O(n) space you don't need. The scalar version is the one that lands in interviews.
- Trying to use division — the problem explicitly disallows it, and zeros in the input break division-based approaches.
- Treating boundary elements as special cases — with the scalar approach they just work: `prefix` starts at 1 (nothing to the left), `postfix` starts at 1 (nothing to the right).

**Time:** O(n) — two linear passes.  
**Space:** O(1) extra — the output array is required by the problem and doesn't count toward space complexity.

---

## Style fixes (apply going forward)

- **`range(len())` without `enumerate`** — still recurring in sub-0/1/2. When you need both index and value, use `enumerate`. When you only need to modify by position (like the prefix pass here), `range(n)` is actually correct — know the difference.
- **`|` for boolean OR** — `|` is bitwise OR. For boolean logic, use `or`. Sub-1's bug came from this exactly.

---

## The pattern + where else it shows up

**Prefix products** is a specialization of the broader prefix sum / running aggregate pattern: precompute cumulative state from one direction, then combine with cumulative state from the other. The key idea is that anything "except self" can be decomposed into "left of self" × "right of self."

Related NC150 problems using the same instinct:
- **Maximum Product Subarray** — tracks running prefix and suffix products to handle negative numbers.
- **Trapping Rain Water** — max water at each column = min(max_left, max_right) − height[i]. Same left/right decomposition.
- **Best Time to Buy and Sell Stock** — prefix minimum (cheapest price seen so far) × current price.

---

## Interview check

- Did you name the brute force first and its complexity before optimizing? (O(n²) → O(n) is the story to tell)
- Could you explain *why* `otp[i] = prefix` comes *before* `prefix *= nums[i]`? That ordering is the whole trick — if you can't articulate it, you don't own the solution yet.
- Did you justify why division isn't used? (problem constraint + zeros — name both)

---

## Question for you

In sub-3, the first loop stores `prefix` into `otp[i]` *before* updating `prefix`. If you swapped those two lines — updated `prefix` first, then stored — what would the output be, and why would it be wrong?

---

## Your turn — fill this in

*(Pre-filled from your submission comments — finish the rest in your own words.)*

**What I tried first:** Brute force O(n²) with ChatGPT assist (sub-0). Then tried to build separate prefix/postfix arrays after watching NeetCode's algorithm explanation (sub-1) — right concept, broken implementation.

**Where I got stuck:** Sub-1 shows you understood prefix × postfix but couldn't get the arrays to actually accumulate running products. The `|` vs `or` bug probably wasn't obvious since the condition looked reasonable.

**What made it click:** *(your words — was it seeing the scalar prefix/postfix version with no extra arrays? understanding why you store prefix before updating it? something else? write it here.)*

**Revisit?** [x] Mark for redo in 1 week — subs 3/4 are the looked-up solution. Can you reproduce the scalar two-pass approach cold, and explain the ordering of store-vs-update?
