#!/usr/bin/env python3
"""
Convert decimal numbers to binary and hexadecimal using basic algorithms.
"""

import sys
import time


def to_binary(number):
    """
    Convert a decimal number to binary representation.
    """
    if number == 0:
        return "0"

    result = ""
    value = number

    while value > 0:
        result = str(value % 2) + result
        value //= 2

    return result


def to_hexadecimal(number):
    """
    Convert a decimal number to hexadecimal representation.
    """
    digits = "0123456789ABCDEF"

    if number == 0:
        return "0"

    result = ""
    value = number

    while value > 0:
        result = digits[value % 16] + result
        value //= 16

    return result


def main():
    """
    Main execution function.
    """
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    start_time = time.time()
    results = []

    with open(sys.argv[1], "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            try:
                number = int(line.strip())
                binary = to_binary(number)
                hexa = to_hexadecimal(number)
                results.append(
                    f"{number} -> Binary: {binary}, Hexadecimal: {hexa}"
                )
            except ValueError:
                print(f"Invalid data at line {line_number}: {line.strip()}")

    elapsed = time.time() - start_time
    results.append(f"\nTime Elapsed: {elapsed:.6f} seconds")

    output = "\n".join(results)
    print(output)

    with open("ConvertionResults.txt", "w", encoding="utf-8") as file:
        file.write(output)


if __name__ == "__main__":
    main()
