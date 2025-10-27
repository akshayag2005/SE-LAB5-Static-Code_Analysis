"""
Inventory Management System Module.

This module provides functions for managing inventory stock data,
including adding, removing, and querying items.
"""

import json
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Add an item to the inventory.

    Args:
        item (str): The item name to add. Defaults to "default".
        qty (int): The quantity to add. Defaults to 0.
        logs (list): Optional list to append log messages. Defaults to None.
    """
    if logs is None:
        logs = []
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """
    Remove a specified quantity of an item from inventory.

    Args:
        item (str): The item name to remove.
        qty (int): The quantity to remove.
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        pass


def get_qty(item):
    """
    Get the quantity of an item in inventory.

    Args:
        item (str): The item name to query.

    Returns:
        int: The quantity of the item.
    """
    return stock_data[item]


def load_data(file="inventory.json"):
    """
    Load inventory data from a JSON file.

    Args:
        file (str): The file path to load from. Defaults to "inventory.json".
    """
    global stock_data  # pylint: disable=global-statement
    with open(file, "r", encoding="utf-8") as f:
        stock_data = json.loads(f.read())


def save_data(file="inventory.json"):
    """
    Save inventory data to a JSON file.

    Args:
        file (str): The file path to save to. Defaults to "inventory.json".
    """
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(stock_data))


def print_data():
    """
    Print a report of all items in inventory.
    """
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])


def check_low_items(threshold=5):
    """
    Check for items below a threshold quantity.

    Args:
        threshold (int): The threshold quantity. Defaults to 5.

    Returns:
        list: A list of items below the threshold.
    """
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result


def main():
    """
    Main function to demonstrate inventory operations.
    """
    add_item("apple", 10)
    add_item("banana", -2)
    # Skipping invalid type operation: add_item(123, "ten")
    # This would cause TypeError: unsupported operand type(s)
    # for +: 'int' and 'str'
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    # Removed eval() - it's a security risk
    print("Eval function removed for security")


if __name__ == "__main__":
    main()
