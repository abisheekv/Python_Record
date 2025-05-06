inventory = {}

def add_product(name, quantity):
    inventory[name] = inventory.get(name, 0) + quantity
    print(f"Added {quantity} of {name}")

def update_product(name, quantity):
    if name in inventory:
        inventory[name] = quantity
        print(f"Updated {name} to {quantity}")
    else:
        print(f"{name} not found in inventory.")

def delete_product(name):
    if name in inventory:
        del inventory[name]
        print(f"{name} removed from inventory")
    else:
        print(f"{name} not found")

def show_inventory():
    return inventory
