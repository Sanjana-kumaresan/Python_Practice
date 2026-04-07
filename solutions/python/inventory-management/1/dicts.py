"""Functions to keep track and alter inventory."""

def create_inventory(items):
    inventory = {}
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


def add_items(inventory, items):
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


def decrement_items(inventory, items):
    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
    return inventory


def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    return inventory


def list_inventory(inventory):
    return [(item, count) for item, count in inventory.items() if count > 0]