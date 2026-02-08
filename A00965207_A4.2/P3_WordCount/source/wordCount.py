#!/usr/bin/env python3
"""
Count distinct words and their frequency from a text file.
"""

import sys
import time


def clean_word(word):
    """
    Normalize a word by converting it to lowercase
    and removing punctuation characters.
    """
    return word.lower().strip(".,!?;:\"()[]{}")


def main():
    """
    Main execution function.
    """
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)

    start_time = time.time()
    frequencies = {}

    with open(sys.argv[1], "r", encoding="utf-8") as file:
        for line in file:
            words = line.split()
            for word in words:
                clean = clean_word(word)
                if clean:
                    frequencies[clean] = frequencies.get(clean, 0) + 1

    elapsed = time.time() - start_time

    results = []
    for word, count in frequencies.items():
        results.append(f"{word}: {count}")

    results.append(f"\nTime Elapsed: {elapsed:.6f} seconds")

    output = "\n".join(results)
    print(output)

    with open("WordCountResults.txt", "w", encoding="utf-8") as file:
        file.write(output)


if __name__ == "__main__":
    main()
