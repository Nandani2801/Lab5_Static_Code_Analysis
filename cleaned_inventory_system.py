"""Inventory System Module
Manages a simple stock inventory system with functions to
add, remove, and display items. Includes file operations
for saving and loading inventory data.
"""

import json
from datetime import datetime

stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add an item to the inventory."""
    if logs is None:
        logs = []
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove a quantity of an item from the inventory."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        pass


def get_qty(item):
    """Return the quantity of a given item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load inventory data from a JSON file."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        stock_data = {}


def save_data(file="inventory.json"):
    """Save current inventory data to a JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)


def print_data():
    """Print the current inventory."""
    print("Items Report")
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")


def check_low_items(threshold=5):
    """Return a list of items below the given threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main execution function for inventory management."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, 10)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()

