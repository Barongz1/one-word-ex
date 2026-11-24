"""One Word From Your Ex — entry for make.fun.

Writes one word to /output/entry.txt.
The word is exactly one word our ex would use to describe us, funny and painfully honest, and nothing else.
"""
import os

WORD = "Unavailable"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD + "\n")

if __name__ == "__main__":
    main()
