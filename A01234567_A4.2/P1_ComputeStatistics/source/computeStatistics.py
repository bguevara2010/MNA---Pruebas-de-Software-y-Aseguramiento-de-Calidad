
#!/usr/bin/env python3
"""
Compute descriptive statistics from a file.
"""

import sys
import time


def read_numbers(file_path):
    """
    Read numeric values from a file.
    Invalid values are reported and ignored.
    """
    numbers = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            try:
                value = float(line.strip())
                numbers.append(value)
            except ValueError:
                print(f"Invalid data at line {line_number}: {line.strip()}")
    return numbers


def mean(numbers):
    """Compute the mean of a list of numbers."""
    total = 0.0
    for number in numbers:
        total += number
    return total / len(numbers)


def median(numbers):
    """Compute the median of a list of numbers."""
    sorted_numbers = sorted(numbers)
    size = len(sorted_numbers)
    mid = size // 2

    if size % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2

    return sorted_numbers[mid]


def mode(numbers):
    """Compute the mode of a list of numbers."""
    frequencies = {}
    for number in numbers:
        frequencies[number] = frequencies.get(number, 0) + 1

    max_count = max(frequencies.values())
    modes = [key for key, value in frequencies.items() if value == max_count]

    return modes[0] if len(modes) == 1 else modes


def variance(numbers, avg):
    """Compute the population variance of a list of numbers."""
    total = 0.0
    for number in numbers:
        total += (number - avg) ** 2
    return total / len(numbers)


def standard_deviation(var):
    """Compute the population standard deviation."""
    return var ** 0.5


def main():
    """Main execution function."""
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        sys.exit(1)

    start_time = time.time()
    numbers = read_numbers(sys.argv[1])

    if not numbers:
        print("No valid numbers found.")
        sys.exit(1)

    avg = mean(numbers)
    med = median(numbers)
    mod = mode(numbers)
    var = variance(numbers, avg)
    std = standard_deviation(var)
    elapsed = time.time() - start_time

    result = (
        f"Mean: {avg}\n"
        f"Median: {med}\n"
        f"Mode: {mod}\n"
        f"Variance (Population): {var}\n"
        f"Standard Deviation (Population): {std}\n"
        f"Time Elapsed: {elapsed:.6f} seconds\n"
    )

    print(result)

    with open("StatisticsResults.txt", "w", encoding="utf-8") as file:
        file.write(result)


if __name__ == "__main__":
    main()
