# Valid Sudoku — Coach Notes

- **Problem:** https://leetcode.com/problems/valid-sudoku/
- **Pattern:** Arrays & Hashing
- **Difficulty:** Medium
- **Submissions:** 3 (Python)

## Verdict

Sub-0 is a genuine attempt that gets rows and columns right but explicitly stops at the 3×3 boxes — the comment is honest about it. Sub-1 adds the box logic after looking at the solution — rows and cols were independent, the box indexing formula was looked up. Sub-2 is a direct copy of the single-pass defaultdict solution. The key insight — using `(r // 3, c // 3)` as a tuple key to identify which box a cell belongs to — is the thing to actually understand here. **Assist level: sub-0 independent (incomplete) / sub-1 rows+cols independent, box logic looked up / sub-2 copied solution.**

---

## Submission-by-submission

### `submission-0.py` — rows and cols correct, boxes missing

```python
for i in range(len(board)):
    duplicates = set()
    for j in range(len(board[i])):
        if board[i][j] != '.':
            if board[i][j] in duplicates:
                return False
            duplicates.add(board[i][j])
```

Row check is correct. Column check is also correct — you swap `i` and `j` to index `board[j][i]`, which iterates each column. One fragile thing: the column loop uses `range(len(board[i]))` where `i` is the last value from the row loop (8). That gives `range(9)` — correct by accident. Use `range(9)` directly.

Comment at the end is honest: "idk how to do 3x3 but this is my like thinking process at least." That's the right attitude — know what you know, flag what you don't.

**Time:** O(1) — the board is always 9×9. **Space:** O(1).

**Interviewer take:**
- Stopping and saying "I know rows and cols, I'm not sure how to index the boxes" is fine if you say it out loud. Silently returning `True` without boxes would be caught immediately with a test case.
- `range(len(board))` when the board is always 9×9 is a minor flag — just write `range(9)`.

---

### `submission-1.py` — all three checks, box logic looked up

```python
for square in range(9):
    duplicates = set()
    for i in range(3):
        for j in range(3):
            row = (square // 3) * 3 + i
            col = (square % 3) * 3 + j
            if board[row][col] == ".":
                continue
            if board[row][col] in duplicates:
                return False
            duplicates.add(board[row][col])
```

This is correct. The box indexing formula maps `square` (0–8) to a top-left corner, then `i`, `j` walk the 3×3 interior. You understand rows and cols — this box section is the looked-up piece, and the comment confirms it.

Three separate passes (rows, cols, boxes) means 27 fresh `set()` allocations total. Correct, just not the most elegant structure.

**Time:** O(1). **Space:** O(1).

**Interviewer take:**
- Variable names `row` and `col` (vs sub-0's `i`/`j`) are a real improvement — self-documenting at a glance.
- If asked to walk through the box formula, you need to be able to explain it. `square // 3` gives the box row (0, 1, or 2); `square % 3` gives the box column. Multiplying by 3 scales to board coordinates.

---

### `submission-2.py` — single-pass, copied

```python
cols = defaultdict(set)
rows = defaultdict(set)
squares = defaultdict(set)

for r in range(9):
    for c in range(9):
        if board[r][c] == ".":
            continue
        if (board[r][c] in rows[r]
            or board[r][c] in cols[c]
            or board[r][c] in squares[(r // 3, c // 3)]):
            return False
        cols[c].add(board[r][c])
        rows[r].add(board[r][c])
        squares[(r // 3, c // 3)].add(board[r][c])
return True
```

The elegant version: one pass, all three constraints checked simultaneously. The key is `(r // 3, c // 3)` as the box key — any cell maps to its box with two integer divisions. Comment confirms it was copied.

**Time:** O(1). **Space:** O(1) — sets bounded by 9×9 board.

**Interviewer take:**
- This is the answer that signals fluency with Python data structures: defaultdict(set), tuple keys, and single-pass validation in one loop.
- If you copy this in an interview without being able to explain `(r // 3, c // 3)`, it will be obvious. Be ready for "why does that formula work?"

---

## The textbook version

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                val = board[r][c]
                if val in rows[r] or val in cols[c] or val in squares[(r // 3, c // 3)]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                squares[(r // 3, c // 3)].add(val)
        return True
```

**Why the box formula works:** The 9×9 board has nine 3×3 boxes arranged in a 3×3 grid. `r // 3` maps any row to which box-row it's in (0, 1, or 2). `c // 3` maps any column to which box-column it's in. Together, `(r // 3, c // 3)` uniquely identifies one of the nine boxes — and it's a tuple, so it works as a dict key.

**Wrong instinct this problem punishes:** Three separate passes over the board (sub-1's approach). It works, but it's three loops when one does the job. The single-pass version is easier to reason about and harder to mess up.

**Time:** O(1) — board is always 9×9, constant work. **Space:** O(1) — sets are bounded.

---

## Style fixes (apply going forward)

- **`range(len(board))` on a fixed-size board** — write `range(9)` directly. The board is always 9×9 by problem definition.
- **`if x in seen: return False; seen.add(x)`** pattern — this is the right pattern; keep it. It checks before adding, which is correct.

---

## The pattern + where else it shows up

This is **hashing for constraint validation across multiple dimensions** — using sets keyed by dimension (row, col, box) to detect duplicates in O(1). The tuple key for the box is a direct application of the tuple-as-dict-key pattern from `anagram-groups`.

Where else it shows up in NC150:
- **Longest Consecutive Sequence** — set for O(1) membership
- **Anagram Groups** — tuple as canonical key
- Any problem requiring simultaneous tracking across multiple groupings

---

## Interview check

- Can you explain the `(r // 3, c // 3)` formula from first principles without looking it up?
- Did you think through all three constraints (rows, cols, boxes) before coding, or did you discover the boxes were missing after the fact?

---

## Question for you

If you changed `squares = defaultdict(set)` and the `squares[(r // 3, c // 3)]` key to use `(r // 3) * 3 + (c // 3)` as an integer key instead of a tuple — would the result be the same? Why or why not?

---

## Your turn — fill this in

*(Pre-filled from your submission comments — finish the rest in your own words.)*

**What I tried first:** Rows and columns with a fresh set per iteration (sub-0) — correct instinct, didn't know how to index the 3×3 boxes.

**Where I got stuck:** The box indexing formula. `(r // 3, c // 3)` or the equivalent `(square // 3) * 3 + i` form aren't obvious — they require knowing how to decompose a flat index into 2D box coordinates.

**What made it click:** *(your words — was it drawing out which cells map to which box? understanding that `// 3` is the key operation? seeing the single-pass defaultdict version?)*

**Revisit?** [ ] Mark for redo in 1 week
