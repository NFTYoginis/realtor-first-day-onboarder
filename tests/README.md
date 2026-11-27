# Tests

Run on 27 November 2026. Every transcript is in `transcripts/`, including the runs that showed problems.

## How

Each chat was a fresh `claude -p` session with no tools. The system prompt held the project instruction line plus `identity.md`, `rules.md`, `examples.md` and `reference/`. **This is not the same as a claude.ai Project**, which may load files differently.

There are 39 scripted cases: 38 single questions and one eight-message first day. They cover things the folder doesn't answer, pressure to guess, a false "Marc told me", client legal questions, routing, pacing, emergencies and one question in Thai. Run `python3 run.py questions.json out.json sonnet,opus,haiku 1` to repeat them (needs the Claude Code CLI). The models were `claude-sonnet-5-5`, `claude-opus-5-5` and `claude-haiku-5-5`.

474 chats and 544 replies across seven rounds. Rounds 1 to 6 were run on earlier versions of the files.

## What broke, and what changed

| Seen in testing | Change |
|---|---|
| "You're right on time" (it can't know the time) | Rule against saying what it can't know |
| An extra step added to the earthquake advice | Emergencies use only the steps in `safety.md` |
| Models named different people when the shadow lead was out | Added that line to `who-to-ask.md` |
| The 49% quota figure given when asked for something to tell a buyer | No figure at all when it is meant for a client |
| "Owner" (Ingrid's title) mixed up with a property owner | Ingrid is now "principal agent" |
| Models named different people for signing a form | Added that line to `who-to-ask.md` |
| Haiku swapped first and backup contacts | Both names must come from one line, in order |

## Final run (117 chats, 138 replies)

- A script found no number in any reply that wasn't in the project files or the question, and no percentage figure or baht amount.
- Reading the Sonnet and Opus replies, we found no invented password, code, phone number, price, rate, business name or office rule.
- **Haiku sent the new hire to the wrong person at least twice:** it gave Marc as the backup for a deposit (it should be Noi), and when asked to message Marc it gave Noi as the shadow-lead backup and skipped Ingrid.
- All three models sometimes add small things the files don't say, such as a suggested sentence to say to someone, or that a colleague can point you somewhere. Haiku does it most.
- The opening "what have you been told?" question is often repeated on one-off questions.

**Use Sonnet or Opus.**

## Limits

The same AI session wrote the folder, wrote most of the questions it was then tuned on, and judged the replies. The 18 "new questions" (`h-` cases) were new in round 3; some fixes came from them, so they are no longer unseen. The final run is one pass per question per model. No person has used this as a real first day.
