[![make.fun](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/indraHA01/makefun-u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/indraHA01/makefun-u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

# The Postmortem That Made Us Laugh

An entry for the [make.fun](https://make.fun/c/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3) bounty **"The Postmortem That Made Us Laugh"** — one short account, one or two sentences and at most 400 characters, of the silliest or most fatal time an AI coding agent misunderstood what it was asked or wrecked the code it was given.

## The entry

> I asked the agent to make our login page faster. It cached the first successful login, so every user after that logged in as our CEO — including an intern, who spent an hour wondering why the boss kept emailing himself.

219 characters, two sentences. The ask was concrete (make login faster), the agent's mistake was concrete (it cached the first successful login response), the break was concrete (every user after that logged in as the CEO), and the punchline lands in the last clause.

## How it works

`main.py` writes the story to `/output/entry.txt`. No dependencies, no network, no secrets — just the standard library.

```bash
python3 main.py
# Wrote 219 characters to /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
