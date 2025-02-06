"""Module providing a function to calculate sales total."""

import json
import sys
import time


def load_json(file_path):
    """Function to load json file"""
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError as e:
        print(f"Error loading {file_path}: {e}")
        sys.exit(1)


def compute_sales(price_catalogue, sales_record):
    """Function to compute sales"""
    total_sales = 0.0
    price_catalogue = {product["title"]: product["price"]
                       for product in price_catalogue}
    for sale in sales_record:
        product_name = sale.get("Product")
        quantity = sale.get("Quantity", 0)

        if product_name in price_catalogue:
            total_sales += price_catalogue[product_name] * quantity
        else:
            print(
                f"Warning: Product '{product_name}' not found.")

    return total_sales


def main():
    """Main function that handles command-line arguments."""
    if len(sys.argv) != 3:
        print("Usage: python computeSales.py <filename>.json <filename>.json")
        sys.exit(1)

    start_time = time.time()
    price_catalogue = load_json(sys.argv[1])
    sales_record = load_json(sys.argv[2])
    total_sales = compute_sales(price_catalogue, sales_record)
    execution_time = time.time() - start_time
    result = (
        f"Total Sales Revenue: ${total_sales:.2f}\n"
        f"Execution Time: {execution_time:.4f} seconds"
    )

    print(result)

    with open("SalesResults.txt", "w", encoding="utf-8") as file:
        file.write(result)


if __name__ == "__main__":
    main()
