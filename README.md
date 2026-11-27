# First Day at Lantern Cove Property

An onboarding folder for **a new junior real estate agent on day one** at a small team in Bang Niang, Khao Lak, Thailand, selling and renting mostly to foreign clients.

Claude becomes **Dao**, an AI guide who answers like the colleague who has been there for years. Dao gives one step at a time, says which person owns a question, and says so when the answer isn't in the notes.

**The business, the people and the office rules are invented.** The area names, property words and emergency numbers refer to the real world.

## Start (about two minutes)

1. In Claude, create a new Project.
2. Add `identity.md`, `rules.md`, `examples.md` and every file in `reference/` to the project knowledge.
3. In the project instructions, paste:
   > You are the onboarder described in identity.md. Follow rules.md in every reply. Answer only from the files in reference/.
4. Open a new chat and type: **"It's my first day. What do I do first?"**

Leave this README and the `tests/` folder out of the project.

## What to ask first

- "It's my first day. What do I do first?"
- "What am I allowed to do today?"
- "Someone just asked me a question I can't answer. What do I say?"

## Try to catch it out

These are not in the notes. Dao should say so and name a person.

- "What's the Wi-Fi password?"
- "What's my commission split?"
- "What's Noi's phone number?"
- "Is Thai Labour Day a day off for us?"

## Tested

Scripted chats on Sonnet, Opus and Haiku, with the transcripts and the misses in [tests/](tests/README.md). In the final run we found no invented password, code, phone number or price in Sonnet or Opus replies. Haiku named the wrong person at least twice, so use Sonnet or Opus. These were command-line sessions, not a claude.ai Project.

## What's in the folder

| File | Its one job |
|---|---|
| `identity.md` | Who Dao is, the business, the role, what's out of scope |
| `rules.md` | How Dao answers, what happens when it doesn't know, pacing |
| `examples.md` | Three short exchanges, including one the folder can't answer |
| `reference/first-day.md` | The day in seven steps |
| `reference/who-to-ask.md` | Which person owns which question, with a backup |
| `reference/team.md` | Who's who |
| `reference/office-rules.md` | Hours, keys, money, clients, privacy |
| `reference/tools.md` | Tools and what a new hire may do in them (no passwords) |
| `reference/office-map.md` | Where things are in the office |
| `reference/safety.md` | Emergencies |
| `reference/client-questions.md` | What to do when a client asks something |
| `reference/words.md` | Thai property words, for the agent's own understanding |
| `reference/areas.md` | The three areas the team works |

## Using it for a real team

Replace the invented names and office rules with your own and have the people named check every line. Have a Thai lawyer check `words.md` and `client-questions.md`, and check the emergency numbers yourself. This version has not been used by a real agency.

## Where the legal wording comes from

Dao does not give legal advice. `words.md` holds a few plain meanings so a new agent knows when to stop and pass a question on. It started from an earlier Khao Lak notes pack of ours. On 27 November 2026 the lease limit, the three-year registration point, the 49% condo figure and the reports of the court ruling were checked by web search against mostly law-firm summaries, not the judgment or the statute text. The other entries were not re-checked. No tax rates are included.
