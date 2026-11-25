"""Write the robot vacuum's excuse to /output/entry.txt.

The excuse is assembled from the three witnesses the vacuum calls in
its own defence: its map, its bumper and its battery. Joined, they
form one deadpan line that ends on the punchline — the cat's corner
is a border, and borders get respected.
"""
import os
from pathlib import Path

# Each clause is the vacuum speaking in its own voice about one part
# of its world: the map it trusts, the bumper that took the hits and
# the battery it shares every decision with.
CLAUSES = (
    "My map calls that corner Cat Territory",
    "my bumper calls it an impact zone",
    "and my battery and I voted unanimously to respect the border",
)


def build_excuse() -> str:
    """Join the clauses into the single-line excuse."""
    return ", ".join(CLAUSES) + "."


def main() -> None:
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build_excuse(), encoding="utf-8")


if __name__ == "__main__":
    main()
