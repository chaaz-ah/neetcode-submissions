# Anagram Groups — Coach Notes

- **Problem:** https://leetcode.com/problems/group-anagrams/
- **Pattern:** Arrays & Hashing
- **Difficulty:** Medium
- **Submissions:** 6 (Python)

> **Before we move on:** The "Question for you" at the bottom of the two-integer-sum notes has never been answered. Go back and fill in that "Your turn" section — the reflection is the point, not a formality.

## Verdict

Six submissions, two of which were bulk-synced later and missed the original review. Sub-0 started with the right instinct (char frequency map) but abandoned before a grouping strategy landed. Sub-1 tried pairwise comparison — wrong abstraction, several overlapping bugs, gave up explicitly. Sub-2 arrived at the correct sorted-string key with GPT help fixing errors. Sub-3 and sub-4 are the count-array NeetCode approach — sub-4 has an `ord(s)` typo (should be `ord(c)`) that raises TypeError on any non-single-char input. Sub-5 is the correct version. Comments on sub-3/4/5 are identical verbatim: "i do not know what a defaultdict is." Six submissions, three of which are variations on a solution the code explains better than the understanding behind it. Assist level: **independent (broken)** for sub-0/1, **GPT-assisted** for sub-2, **looked up solution** for sub-3/4/5.

## Submission-by-submission

### `submission-0.py` — Right first instinct, no finish line

```python
for i, string in enumerate(strs):
    char = {}
    for j in range(len(string)):
        char[string[j]] = 1 + char.get(string[j], 0)

# this is what i initially thought but maybe i can try using the one-pass counter from the anagram example
```

- Building a per-string character frequency map is exactly the right first thought — same instinct as is-anagram.
- The gap: `char` gets rebuilt each iteration and is never used for anything. There's no grouping logic and no return. The comment shows the thinking was pointing somewhere useful (connecting to the is-anagram pattern), but the submission was abandoned before a key question got answered: *what do I use as the grouping key?*
- `for j in range(len(string))` when you just want the characters — use `for c in string`.
- `final = [[]]` is dead scaffolding that never gets touched.

**Time:** N/A — code is incomplete. **Space:** O(k) per string for `char`, but nothing is stored across iterations.

---

### `submission-1.py` — pairwise comparison, abandoned

```python
for i, string_1 in enumerate(strs):
    char_1 = {}
    for j, string_2 in enumerate(strs, i+1):
        char_2 = {}
        if len(string_1) == len(string_2):
            for j in range(len(string_1)):
                char_1[string_1[j]] = 1 + char_1.get(string_1[j], 0)
                char_2[string_2[j]] = 1 + char_2.get(string_2[j], 0)
            if char_1 == char_2:
                final.append([])
                final[i].append([string_1, string_2])
#yea claude im stuck imma js look at the soltuion for the next submission and submit that
```

- Pairwise comparison is the wrong abstraction — checking every pair is O(n²) and still can't group correctly. The right model is: assign every string a *canonical key*; one pass through the list puts each string in the right bucket.
- `enumerate(strs, i+1)` starts the *counter* at i+1 but iterates **all** of strs, including strings before index i. Intent was to skip already-seen pairs; `strs[i+1:]` would do that. This compares every pair twice.
- `j` is immediately shadowed: used first as the loop variable from `enumerate`, then overwritten by `for j in range(len(string_1))` inside the body. The outer `j` (string_2) is dead after the first inner statement.
- `char_1` is declared in the outer loop but updated inside the inner loop without resetting. By the second inner iteration it holds stale counts from the previous `string_2`, so comparisons are wrong from the start.
- Grouping logic is broken: `final[i].append([string_1, string_2])` appends a nested pair into a single slot rather than a flat group; `final.append([])` just grows the outer list without relating to anything.
- Assist level: **independent attempt (broken, abandoned)**.

**Time/Space:** N/A — incorrect and abandoned.

---

### `submission-2.py` — Correct approach, GPT-assisted

```python
map = {}
for i, string in enumerate(strs):
    key = "".join(sorted(string))
    if key not in map:
        map[key] = []
    map[key].append(string)
return list(map.values())
```

- Sorted string as key is correct and clean. Anagrams produce identical sorted strings, so this groups them reliably.
- `map` shadows the Python builtin — open style debt, fourth problem in a row. Use `groups`, `res`, `freq`.
- The explicit `if key not in map: map[key] = []` guard works, but `defaultdict(list)` eliminates it entirely (see sub-3).
- `final = [[]]` is still sitting at the top as dead code — never used, never cleaned up.
- The comment says it all: *"bruh lwk did it with seeing the algorithm english of the first solution and kinda asking gpt to fix a lot of the errors."* The approach is right; independent reproduction is the open question.

**Time:** O(m·k·log k) — m strings, each sorted in O(k·log k). **Space:** O(m·k) for the hashmap.

---

### `submission-3.py` — Right tool, unknown why

```python
res = defaultdict(list)
for s in strs:
    sortedS = ''.join(sorted(s))
    res[sortedS].append(s)
return list(res.values())
# i do not know what a defaultdict is
# also explain the list(res.values())
```

- `defaultdict(list)` is the clean version of sub-2's `if key not in map` guard. When you access a missing key, it auto-initializes it with an empty list. That's all it does. See SYNTAX.md.
- `list(res.values())`: `res.values()` returns a *view object* — a live reference into the dict, not an actual list. LeetCode expects `List[List[str]]`, so `list()` converts the view into one. That's the whole thing.
- The comment says this wasn't independently written. The code is idiomatic; the understanding of what it's doing is the gap.

**Time:** O(m·k·log k). **Space:** O(m·k).

---

### `submission-5.py` — Optimal solution, "why" still missing

```python
res = defaultdict(list)
for s in strs:
    count = [0] * 26
    for c in s:
        count[ord(c) - ord('a')] += 1
    res[tuple(count)].append(s)
return list(res.values())
# also the tuple
```

- The 26-slot count array is the optimal approach. Instead of sorting, you build a fixed-length array where index 0 = 'a', index 1 = 'b', etc. All anagrams produce the exact same array.
- `tuple(count)`: dict keys must be hashable. Lists are mutable, so they're not hashable — `res[count]` would raise `TypeError`. `tuple` is immutable, so it can be hashed. That's why `tuple(count)` works. See SYNTAX.md.
- `ord(c) - ord('a')`: `ord()` gives the ASCII integer for a character. `ord('a')` is 97. So `ord('e') - ord('a')` = 4, putting 'e' at index 4 in the array. Every character gets a fixed slot.
- This avoids the O(k·log k) sort — strictly better when strings are long.

**Time:** O(m·k) — m strings, each character processed once. **Space:** O(m·k) for the hashmap.

---

## The textbook version

Two approaches worth knowing cold:

**Approach 1 — Sorted string key:**
```python
from collections import defaultdict

def groupAnagrams(strs):
    res = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))   # anagrams → identical sorted form
        res[key].append(s)
    return list(res.values())
```
Why it works: sorting a string produces a canonical form. All strings with the same letters in any order sort to the same thing. **O(m·k·log k) time, O(m·k) space.**

**Approach 2 — Count array key (optimal):**
```python
from collections import defaultdict

def groupAnagrams(strs):
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        res[tuple(count)].append(s)
    return list(res.values())
```
Why it works: same letter frequencies → identical count array → identical tuple key. No sort needed. **O(m·k) time, O(m·k) space.**

The wrong instinct this problem punishes: comparing strings pairwise. That's O(m²·k) — you end up checking every pair instead of letting the hashmap do the grouping for you. The insight is that you don't need to compare strings to each other at all — you just need a canonical form they all agree on.

## Style fixes (apply going forward)

- **`map = {}`** — `map` is a Python builtin. Four problems in a row now. Use `res`, `groups`, `freq`.
- **Dead code** — `final = [[]]` was never used; delete leftover scaffolding before submitting.
- **`for j in range(len(string))`** — when you just want characters, `for c in string` is cleaner.

## The pattern + where else it shows up

**Canonical key grouping** — the core instinct is: *what representation will all equivalent items agree on?* Once you have that, a `defaultdict(list)` handles the grouping automatically. You don't compare items to each other; you let the key do the work.

Same instinct in NC150:
- **Valid Anagram** — same frequency-map pattern, single pair instead of a group
- **Top K Frequent Elements** — build a frequency map, then extract by rank
- **Encode and Decode Strings** — canonical encoding so different strings don't collide at decode time

## Interview check

- Naming a variable `map` blocks a Python builtin and signals unfamiliarity to an interviewer. Costs nothing to fix.
- When you reach for `defaultdict`, be ready to explain it in one sentence: *"It's a dict that auto-initializes missing keys, so I don't need an explicit guard."*
- The `tuple(count)` trick is worth explaining unprompted: *"I'm using a tuple because dict keys need to be hashable, and lists aren't."*

## Question for you

Sub-5 uses `ord(c) - ord('a')` to map each character to an index. Walk through the string `"eat"` character by character — what does `count` look like after the loop finishes? Then explain why `tuple(count)` for `"eat"` and `tuple(count)` for `"tea"` will be identical.

## Your turn — fill this in

*(Pre-filled from your submission comments — finish the rest in your own words.)*

**What I tried first:** Building a character frequency map for each string (sub-0) — the char-count instinct from is-anagram. Right idea, but no plan for what to use as a grouping key or how to connect matching strings.

**Where I got stuck:** Knowing anagrams have the same character counts is one thing — knowing what to *do* with that (use it as a dict key, group under it) is where it stalled.

**What made it click:** *(your words — was it the sorted-string key? realizing all anagrams sort to the same thing? seeing the defaultdict pattern? write it here.)*

**Revisit?** [x] Mark for redo in 1 week — sub-2 was GPT-assisted, sub-3/sub-5 are NeetCode solutions with explicit gaps (defaultdict, tuple, list(values())). The pattern hasn't been independently reproduced yet.
