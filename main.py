"""One-line entry for The Funniest One-Line Resignation Letter: writes the line the judge reads to /output/entry.txt."""

import os

LINE = (
    "I resign effective immediately \\u2014 my code reviews of my own commits proved the only thing I ship is confidence."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
