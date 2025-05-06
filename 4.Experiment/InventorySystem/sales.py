from product import inventory

def sell_product(name, quantity):
    if name in inventory and inventory[name] >= quantity:
        inventory[name] -= quantity
        print(f"Sold {quantity} of {name}")
    else:
        print(f"Not enough {name} in stock or product not found.")
