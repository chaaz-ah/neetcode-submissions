# SYNTAX.md — Python patterns aakesh has gaps in

Maintained by the coach. Added to when submission comments or code reveal a syntax gap. Never edited by the user.

---

## defaultdict
Use when you want a dict that auto-initializes missing keys — no need to check if key exists first.
```python
# instead of:
if key not in d:
    d[key] = 0
d[key] += 1

# use:
from collections import defaultdict
d = defaultdict(int)   # int → default 0
d[key] += 1

# also useful:
d = defaultdict(list)  # list → default []
d[key].append(val)
```

---

## ''.join(sorted(s))
Sorts a string's characters alphabetically and rejoins as a new string. Common for anagram checks.
```python
# sorted(s) → list of chars in alphabetical order
# ''.join(...) → collapses list back into a string

''.join(sorted("anagram"))  # → 'aaaganmr'
''.join(sorted("nagaram"))  # → 'aaaganmr'  (same → anagram)
```

---

## tuple() as a dict key
Use when you need to use a list as a dict key — lists aren't hashable, tuples are.
```python
# instead of: res[count]  → TypeError: unhashable type: 'list'

# use:
res[tuple(count)]  # tuple is immutable → hashable → valid dict key

# common pattern: fixed-size count array as a canonical key
count = [0] * 26
for c in s:
    count[ord(c) - ord('a')] += 1
res[tuple(count)].append(s)
```

---

## dict.values() and list()
`dict.values()` returns a *view* — a live reference to the dict's values, not a standalone list.
```python
# if the return type needs List[...], wrap it:
return list(res.values())   # converts view → actual list

# res.values() alone works for iteration, but not when a list is required
```

---

## dict.items() vs range(len())
Use `.items()` to iterate over a dict; use `range(len())` for lists indexed by position.
```python
# instead of: for i in range(len(freq)):  → KeyError (dict keys aren't 0,1,2,...)
freq = defaultdict(int)
freq[3] += 2
freq[1] += 1
# freq[0] is just a new key with value 0 — not the first element

# use .items() to get every (key, value) pair from a dict:
for num, count in freq.items():
    print(num, count)   # (3, 2) then (1, 1)

# range(len()) is for lists, where keys ARE 0,1,2,...:
lst = [10, 20, 30]
for i in range(len(lst)):
    print(lst[i])       # fine — lst[0], lst[1], lst[2] exist
```

---

## `|` vs `or` (bitwise OR vs boolean OR)

Use `or` for boolean logic. `|` is bitwise OR — has *higher* precedence than `!=`, `==`, and other comparisons, which causes silent bugs.
```python
# WRONG — i != 0 | i != len(nums)-1
# parses as: i != (0 | i) != len(nums)-1
#          = i != i != len(nums)-1   → always False (i == i is always True)

# use 'or' for boolean conditions:
if i != 0 or i != len(nums) - 1:   # correct

# bitwise | is for operating on the bits of integers, not for conditions:
0b1010 | 0b0101  # → 0b1111 (bit-level)
```

---

## heapq (min-heap)
Python's `heapq` is always a min-heap — smallest element is at the root and comes out first on pop.
```python
import heapq

# push: add an element (tuples sort by first element)
heapq.heappush(heap, (count, value))

# pop: removes and returns the SMALLEST element
heapq.heappop(heap)    # returns (count, value) with the lowest count

# top-k pattern — two heappops, two different jobs:
heap = []
for num, cnt in count.items():
    heapq.heappush(heap, (cnt, num))
    if len(heap) > k:
        heapq.heappop(heap)   # PRUNING — drop the least frequent to maintain size k

result = [heapq.heappop(heap)[1] for _ in range(k)]   # EXTRACTION — drain what's left
# After the build loop, heap holds exactly the k most frequent elements.
# The two pops do completely different things — don't confuse them.
```

---

## `isalnum()` — alphanumeric check in one call
Use when you need to keep only letters and digits and discard everything else.
```python
# instead of:
char.isalpha() or char.isnumeric()

# use:
char.isalnum()   # True for a-z, A-Z, 0-9 — same result, one method

# common pattern for palindrome filtering:
filtered = "".join(c.lower() for c in s if c.isalnum())
```

---

## Don't shadow `reversed`
`reversed` is a Python builtin that returns a reverse iterator. Naming a variable `reversed` hides it.
```python
# instead of:
reversed = s[::-1]   # shadows the builtin

# use:
rev = s[::-1]
# or just: return s == s[::-1]  (no variable needed)
```

---