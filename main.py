"""The Postmortem That Made Us Laugh — make.fun entry.

Writes one short agent-disaster story (two sentences, under 400
characters) to /output/entry.txt, as the competition requires.

The story: an agent asked to speed up a login page "optimises" it by
caching the first successful login, so every user afterwards logs in
as the CEO. Concrete ask, concrete wrong action, concrete break, and
a punchline in the last clause.
"""

import os

STORY = (
    "I asked the agent to make our login page faster. "
    "It cached the first successful login, so every user after that "
    "logged in as our CEO \u2014 including an intern, who spent an hour "
    "wondering why the boss kept emailing himself."
)


def main() -> None:
    """Write the entry story to /output/entry.txt."""
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(STORY)
    print(f"Wrote {len(STORY)} characters to {path}")


if __name__ == "__main__":
    main()
