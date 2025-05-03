from Product_Details.entry_display import products, add_product, display_products
from Product_Details.update_delete import update_product, delete_product
from Purchase_Billing.billing import adding_product
while True:
  print("1.Add Product\n2.Display Products\n3.Update Product\n4.Delete Product\n5.Purchase\n6.Exit")
  ch=input("Enter your choice:")
  if ch=='1':
    add_product()
  elif ch=='2':
    display_products()
  elif ch=='3':
    update_product()
  elif ch=='4':
    delete_product()
  elif ch=='5':
    adding_product()
  elif ch=='6':
    print("Thanks for coming.")
    break
  else:
    print("Invaild choice.")