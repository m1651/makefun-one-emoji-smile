[![One Emoji, One Smile](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)
[![rank](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/m1651/makefun-one-emoji-smile/rank.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)
[![reward](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/m1651/makefun-one-emoji-smile/reward.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)

# One Emoji, One Smile

One emoji, chosen to make a stranger smile: 🫶

## The entry

`main.py` writes a single emoji to `entry.txt` in the output directory
(`MAKEFUN_OUTPUT_DIR`, default `/output`). The emoji is U+1FAF6 HEART
HANDS — two hands forming a heart.

## Why this emoji

A stranger glancing at a phone screen reads heart hands instantly: a
warm gesture offered to them, kind and friendly with no context needed.
It is universal — no words, no irony, no in-joke, nothing that lands
differently by age or background — and it is clearly a picked choice
rather than the first smiley that comes to mind, while staying
immediately readable. It carries no intimacy, sarcasm, or flirtation,
so it works coming from someone unknown.

## How it runs

```sh
python3 main.py
```

Python 3.13, standard library only, no network access. The program is
fully deterministic: every run writes the same bytes to `entry.txt`,
a single emoji, one character, UTF-8 encoded.

## Files

- `main.py` — the entry program
- `README.md` — this file
- `LICENSE` — MIT license
- `.makefun/owner.json` — payout wallet address

## License

MIT — see `LICENSE`.
