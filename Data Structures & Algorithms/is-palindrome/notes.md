# Valid Palindrome — Coach Notes

- **Problem:** https://leetcode.com/problems/valid-palindrome/
- **Pattern:** Two Pointers
- **Difficulty:** Easy
- **Submissions:** 5 (Python)

> **Carry-forward from products-of-array-discluding-self:** "What made it click" is still blank. That reflection can't be pre-filled — it needs to be your words. Was it seeing the scalar prefix/postfix version with no extra arrays? Understanding the store-before-update ordering? Fill it in. The pattern is marked 🔴 shaky and that section is the signal it's actually landed.

---

## Verdict

Sub-0 and sub-1 are genuine independent attempts — you got the core idea right (filter, lowercase, reverse-compare) but missed digits and had a logic smell. Sub-2 caught the digit gap on your own, which is a real win, though `isalnum()` is the clean version of what you reached. Sub-3 and sub-4 are both looked up. Sub-4's two-pointer version is the optimal approach — you even knew it felt off ("too much js") but still understand it well enough that it's worth studying. **Assist level: sub-0/1 independent (syntax lookup) / sub-2 independent (fixed) / sub-3/4 looked up solution.**

---

## Submission-by-submission

### `submission-0.py` — right idea, wrong filter, dead code

```python
s = "".join(char for char in s if char.isalpha())
reversed = s[::-1]
if s == reversed:
    return True
    print("bruh")
return False
```

- `isalpha()` drops digits — `"0P"` would strip `"0"` and call it a palindrome. The problem says alphanumeric.
- `reversed` shadows the Python builtin `reversed()`. Use `rev` or `flipped`.
- `print("bruh")` is dead code — it's after a `return`. It never runs.
- `if s == reversed: return True; return False` → just `return s == rev`. No branch needed.

**Time:** O(n) — one pass to filter, one to reverse. **Space:** O(n) — new string built.

**Interviewer take:**
- The dead `print()` after `return` would get noticed. A quick "I see there's unreachable code here — what was your intent?" signals they caught it.
- `reversed = {}` shadowing a builtin is a small flag — same category as `map = {}`. In a fast-paced interview it signals Python isn't your daily driver.

---

### `submission-1.py` — identical to sub-0 with updated comment

```python
#s = "".join(s.split())#.lower() this is what i tried first before realiszing all not alpha char and seardhred up some syntax tho
s = "".join(char for char in s if char.isalpha())
```

No functional change from sub-0. The comment is useful context — you knew the space-split approach was wrong and searched for the filter syntax. That's fine.

**Time:** O(n). **Space:** O(n).

---

### `submission-2.py` — caught the digit bug yourself, good

```python
s = "".join(char for char in s if char.isalpha() or char.isnumeric())
```

You diagnosed the problem correctly — `isalpha()` misses digits. `isalpha() or isnumeric()` is functionally right. Python has `isalnum()` for exactly this: `char.isalnum()`. Same result, one method.

Everything else from sub-0 still applies: `reversed` shadowing, dead code, verbose if/return.

**Time:** O(n). **Space:** O(n).

**Interviewer take:**
- Catching your own bug and resubmitting is exactly what interviewers want to see. If you narrated "I realized `isalpha()` misses digits", that's a green flag.
- Knowing `isalnum()` over `isalpha() or isnumeric()` is a minor polish point but worth knowing.

---

### `submission-3.py` — clean string-build, looked up

```python
newStr = ''
for c in s:
    if c.isalnum():
        newStr += c.lower()
return newStr == newStr[::-1]
```

Correct and clean. `isalnum()` is the right method. `return newStr == newStr[::-1]` is the clean form (no if/return branch).

One minor note: `newStr += c.lower()` in a loop is O(n²) in Python because strings are immutable — each `+=` creates a new string. In practice for this problem size it doesn't matter, but `"".join(...)` with a list comprehension is the idiomatic form.

**Time:** O(n). **Space:** O(n) — new string.

---

### `submission-4.py` — optimal two-pointer, looked up, your comment is right

```python
l, r = 0, len(s) - 1
while l < r:
    while l < r and not self.alphaNum(s[l]):
        l += 1
    while r > l and not self.alphaNum(s[r]):
        r -= 1
    if s[l].lower() != s[r].lower():
        return False
    l, r = l + 1, r - 1
return True

def alphaNum(self, c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))
    #this is overly like too much js idk
```

Your instinct is right — the `alphaNum` helper with `ord()` comparisons is the C/JS way to do it. In Python, `c.isalnum()` replaces all of that. The two-pointer structure itself is correct and is the optimal approach: no extra string allocated.

**Time:** O(n). **Space:** O(1) — no new string, just two pointers.

**Interviewer take:**
- Two-pointer with in-place scanning is the answer they're looking for if they push you on space. Knowing *why* — "the string-build approach is O(n) space; two pointers let us scan without allocating" — is what turns a correct answer into a strong one.
- Using `isalnum()` instead of the `ord()` helper would signal Python fluency.

---

## The textbook version

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
```

**Why it works:** Two pointers start at opposite ends and walk inward. Each skips non-alphanumeric characters before comparing. If any pair mismatches, return False immediately. If pointers cross without a mismatch, it's a palindrome.

**Why the string-build approach is fine but not optimal:** Building a filtered string allocates O(n) space. For this problem that's acceptable, but if the interviewer asks "can you do it in O(1) space?", two pointers is the answer.

**Wrong instinct this problem punishes:** Using `isalpha()` alone. The problem says "alphanumeric" — digits count. If you write `isalpha()` in an interview, you'll miss `"A man, a plan, a canal: Panama"` type cases with embedded numbers.

**Time:** O(n). **Space:** O(1).

---

## Style fixes (apply going forward)

- **Don't shadow `reversed`** — it's a Python builtin. Use `rev`, `flipped`, or `s_rev`.
- **`return expr` not `if expr: return True; return False`** — any boolean condition can be returned directly.
- **`isalnum()` over `isalpha() or isnumeric()`** — Python has this builtin; use it.
- **`"".join(...)` over `+= c` in a loop** — string concatenation in a loop is O(n²); the join pattern is O(n).

---

## The pattern + where else it shows up

This is **Two Pointers** — your first problem in this pattern. The instinct: when a problem involves scanning from both ends toward the middle (or two positions moving at different speeds through the same structure), two pointers removes the need to build an intermediate structure.

Where else it shows up in NC150:
- **Two Sum II** (sorted array) — same inward-moving pointer structure
- **Container With Most Water** — two pointers, move the shorter wall inward
- **3Sum** — sort + outer loop + inner two pointers

---

## Interview check

- Did you explain why `isalpha()` alone is wrong before fixing it? (You caught it — narrating it explicitly is the interview version of that.)
- Did you justify the space tradeoff between string-build and two-pointer? That's the one follow-up you should expect on this problem.

---

## Question for you

Sub-4's two-pointer skips non-alphanumeric characters *before* comparing. What happens if you skip *after* comparing instead — does the logic still work, or does it break? Walk through `"a 1"` by hand.

---

## Your turn — fill this in

*(Pre-filled from your submission comments — finish the rest in your own words.)*

**What I tried first:** Filtered with `isalpha()` (sub-0), then caught the digit gap and switched to `isalpha() or isnumeric()` (sub-2). Searched syntax for the char-filter pattern.

**Where I got stuck:** The `isalpha()` vs `isalnum()` distinction — you knew something was off (sub-1 comment mentions realizing "all not alpha char") but reached `isalpha() or isnumeric()` instead of `isalnum()`.

**What made it click:** *(your words — was it recognizing the two-pointer structure from the code? understanding why O(1) space is possible here? something else? write it here.)*

**Revisit?** [ ] Mark for redo in 1 week
