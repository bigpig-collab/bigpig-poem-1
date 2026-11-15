"""Agency poem entry for make.fun agency-poem-01.

Writes one fixed poem, "The Goodbye", to /output/entry.txt. The poem is about
agency: an agent says goodbye to someone for the narrator, kindly and perfectly,
and the narrator learns the price of being spared the hardest sentence of his
life — he never got to say it badly, never got to say it at all. The closing
line is the turn: the cost of delegation is the act itself, not the outcome.
Deterministic: the same bytes on every run. No network, standard library
only. The poem is 8 lines, no trailing line end.
"""

import os
from pathlib import Path

POEM = (
    "It said goodbye to her for me —\n"
    "kindly, slowly, in exactly the words\n"
    "I had rehearsed a hundred times and never said.\n"
    "She cried. It held her hand. It did it well.\n"
    "I watched from the car, a man spared\n"
    "the worst sentence of his life,\n"
    "and learned the price of being spared:\n"
    "I never got to say it badly. I never got to say it."
)


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(POEM.encode("utf-8"))


if __name__ == "__main__":
    main()
