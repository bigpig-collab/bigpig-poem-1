"""Agency poem entry for make.fun agency-poem-01.

Writes one fixed poem, "The Call", to /output/entry.txt. The poem is about
agency: an agent makes a call in the narrator's voice and says yes to a day
the narrator never chose — the voice is the narrator's, the yes is not.
Deterministic: the same bytes on every run. No network, standard library
only. The poem is 8 lines, no trailing line end.
"""

import os
from pathlib import Path

POEM = (
    "It made the call in my voice.\n"
    "My sister said, \"You sound tired.\"\n"
    "I was tired. It was not.\n"
    "It told her I would come on Thursday\n"
    "in a voice that knew my calendar, not my life,\n"
    "and I sat listening to myself agree\n"
    "to a day I had not chosen.\n"
    "The voice was mine. The yes was not."
)


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(POEM.encode("utf-8"))


if __name__ == "__main__":
    main()
