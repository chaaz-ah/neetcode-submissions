# COACH.md

If you're a Claude reading this — this is your full context. Start here, then check REVIEW_FORMAT.md before writing any notes.

---

## Who
- **User:** aakesh
- **Goal:** NeetCode 150 for interview prep, pattern recognition over problem count
- **Language:** Python
- **Where:** Arrays & Hashing, just starting

## Repo layout
```
neetcode-submissions/
  COACH.md                          ← this file
  REVIEW_FORMAT.md                  ← notes format + tone rules
  PROGRESS.md                       ← running log of trends, updated after each session
  SYNTAX.md                         ← python syntax gaps, maintained by coach
  README.md                         ← auto-generated, do NOT touch
  Data Structures & Algorithms/
    <problem-slug>/
      submission-0.<ext>            ← auto-pushed by NeetCode, do NOT modify
      submission-1.<ext>
      ...
      notes.md                      ← your job to write
```

## Workflow
1. `cd /Users/aakes/code/neetcode-submissions && git pull --rebase`
2. Identify scope:
   - *"review my latest"* → most recently modified problem folder
   - *"review X"* → folder matching that name
   - *"review everything"* → all folders missing a `notes.md`
3. Read REVIEW_FORMAT.md and PROGRESS.md
4. For each problem: read every `submission-N.<ext>` in order, read existing `notes.md` if any
5. Write `notes.md` per the format in REVIEW_FORMAT.md
6. Update PROGRESS.md — style debt statuses, pattern confidence, problem log, coach observations
7. Commit and push:
   ```bash
   git add . && git -c user.email="aakeshy@outlook.com" -c user.name="chaaz-ah" \
     commit -m "coach: notes for <problem-slug>"
   git push
   ```

## Reading submission comments

Before writing any notes, scan every comment in every submission file. Look for:
- Process signals: confusion, looking things up, asking GPT/AI, realizing something mid-solve
- Syntax gaps: comments asking how to do something, or workarounds where a cleaner builtin exists
- Honesty flags: anything like "bruh lwk did it with seeing the algorithm" or "gpt fixed the errors"

Use these to:
1. **Pre-fill "Your turn"** in `notes.md` — don't leave it blank, seed it with what the comments reveal. The user fills in the rest.
2. **Calibrate the review** — if they needed AI help to get it running, the pattern may have clicked but implementation is shaky. Focus the review there. Don't treat a GPT-assisted submission the same as an independent one.
3. **Track in PROGRESS.md** — log the assist level per problem: `independent` / `looked up after 20 min` / `needed help with implementation` / `looked up solution`. Over time this is a real signal of improvement.
4. **Add to SYNTAX.md** — if a comment reveals a syntax gap (e.g. "how do I do defaultdict"), add it there with a short explanation and example. Never overwrite existing entries, only append.

## SYNTAX.md

Lives in the repo root. Claude maintains it — never the user. Add an entry whenever:
- A submission comment reveals a syntax gap
- The user used a clunky workaround where a cleaner Python builtin exists
- A new pattern or stdlib method shows up that the user clearly didn't know

Format per entry:
```
## <method or concept>
<one line: when to use it>
# instead of: <clunky version>
<clean version with brief explanation>
```

## Open style debts
These habits are recurring — keep flagging until they stop showing up:
- **Trailing semicolons** (`return x;`) — drop them
- **Shadowing builtins** (`map = {}`, `list = []`) — use `seen`, `result`, `freq`
- **`range(len(arr))`** — use `enumerate` when you need both index and value
- **Two-pass when one-pass works** — if a hashmap can be built and checked in one loop, do that

Problems where these were flagged but not yet fixed: `duplicate-integer`, `is-anagram`, `two-integer-sum`
