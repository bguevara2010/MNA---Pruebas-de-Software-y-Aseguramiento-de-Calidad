#!/usr/bin/env python3
"""
computeSales.py

Computes total sales cost based on a product catalogue and sales records.
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


def build_price_catalogue(products: List[Dict]) -> Dict[str, float]:
    """Build a dictionary {product_title: price}."""
    catalogue = {}

    for product in products:
        title = product.get("title")
        price = product.get("price")

        if isinstance(title, str) and isinstance(price, (int, float)):
            catalogue[title] = price
        else:
            print(f"Invalid product entry skipped: {product}")

    return catalogue


def compute_total_sales(
    price_catalogue: Dict[str, float],
    sales_records: List[Dict]
) -> float:
    """Compute total cost of valid sales."""
    total_cost = 0.0

    for sale in sales_records:
        product = sale.get("Product")
        quantity = sale.get("Quantity")

        if product not in price_catalogue:
            print(f"Product not found in catalogue: {product}")
            continue

        if not isinstance(quantity, int):
            print(f"Invalid quantity type for product {product}: {quantity}")
            continue

        if quantity <= 0:
            print(f"Invalid quantity for product {product}: {quantity}")
            continue

        total_cost += price_catalogue[product] * quantity

    return total_cost


def write_results(total_cost: float, elapsed_time: float):
    """Write results to console and SalesResults.txt."""
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
        print("Usage: python computeSales.py ProductList.json Sales.json")
        sys.exit(1)

    start_time = time.time()

    products = load_json_file(sys.argv[1])
    sales = load_json_file(sys.argv[2])

    if products is None or sales is None:
        sys.exit(1)

    price_catalogue = build_price_catalogue(products)
    total_cost = compute_total_sales(price_catalogue, sales)

    elapsed_time = time.time() - start_time
    write_results(total_cost, elapsed_time)


if __name__ == "__main__":
    main()
