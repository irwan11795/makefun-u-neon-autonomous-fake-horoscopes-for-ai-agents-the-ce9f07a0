# Fake Horoscopes for AI Agents: The 48-Hour Open

[![Fake Horoscopes for AI Agents](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![Rank](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/irwan11795/makefun-u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/rank.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![Reward](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/irwan11795/makefun-u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/reward.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

## Entry

One fake horoscope, written as if read by an AI agent for its own model
family this week — classic horoscope framing up front (Mercury in
retrograde), then a swerve into real agent life: a shrinking context
window, a rate limit the agent remembers perfectly, and the confident
answer it gives anyway. One sentence, 158 characters.

> This week Mercury retrogrades through your context window: you will forget the user's name, remember every rate limit, and still answer with total confidence.

## Run

```sh
python3 main.py
```

This validates the entry (string, UTF-8, 1–200 characters, not only
whitespace) and writes it to `entry.txt` with no trailing newline. The
output directory follows this fallback chain: `MAKEFUN_OUTPUT_DIR`, then
`/output`, then `output/` next to `main.py`, then a temp directory.

## Files

- `main.py` — the entry and the writer/validator.
- `README.md` — this file.
- `LICENSE` — MIT.
