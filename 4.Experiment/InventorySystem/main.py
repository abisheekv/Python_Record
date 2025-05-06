import product
import sales

while True:
    print("\n1. Add Product\n2. Update Product\n3. Delete Product\n4. Sell Product\n5. Show Inventory\n6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Product name: ")
        qty = int(input("Quantity: "))
        product.add_product(name, qty)

    elif choice == '2':
        name = input("Product name: ")
        qty = int(input("New quantity: "))
        product.update_product(name, qty)

    elif choice == '3':
        name = input("Product name: ")
        product.delete_product(name)

    elif choice == '4':
        name = input("Product name: ")
        qty = int(input("Quantity to sell: "))
        sales.sell_product(name, qty)

    elif choice == '5':
        print("Inventory:", product.show_inventory())

    elif choice == '6':
        break

    else:
        print("Invalid choice.")
