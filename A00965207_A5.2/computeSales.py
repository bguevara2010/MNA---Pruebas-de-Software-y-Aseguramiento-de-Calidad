#!/usr/bin/env python3
"""
computeSales.py

Computes total sales cost based on a price catalogue and sales record.
"""

import json
import sys
import time
from typing import Dict, List


def load_json_file(file_path: str):
    """Load a JSON file safely."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as error:
        print(f"Error loading file {file_path}: {error}")
        return None


def compute_total_sales(
    price_catalogue: Dict[str, float],
    sales_records: List[Dict[str, int]]
) -> float:
    """Compute total cost of sales."""
    total_cost = 0.0

    for sale in sales_records:
        product = sale.get("product")
        quantity = sale.get("quantity")

        if product not in price_catalogue:
            print(f"Product not found in catalogue: {product}")
            continue

        if not isinstance(quantity, int) or quantity < 0:
            print(f"Invalid quantity for product {product}: {quantity}")
            continue

        total_cost += price_catalogue[product] * quantity

    return total_cost


def write_results(total_cost: float, elapsed_time: float):
    """Write results to file and console."""
    output = (
        "\n===== SALES RESULTS =====\n"
        f"Total Sales Cost: ${total_cost:.2f}\n"
        f"Execution Time: {elapsed_time:.6f} seconds\n"
    )

    print(output)

    with open("SalesResults.txt", "w", encoding="utf-8") as file:
        file.write(output)


def main():
    """Main program execution."""
    if len(sys.argv) != 3:
        print("Usage: python computeSales.py priceCatalogue.json salesRecord.json")
        sys.exit(1)

    start_time = time.time()

    price_catalogue = load_json_file(sys.argv[1])
    sales_records = load_json_file(sys.argv[2])

    if price_catalogue is None or sales_records is None:
        sys.exit(1)

    total_cost = compute_total_sales(price_catalogue, sales_records)

    elapsed_time = time.time() - start_time
    write_results(total_cost, elapsed_time)


if __name__ == "__main__":
    main()
