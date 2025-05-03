from Product_Details.entry_display import products, display_products
def update_product():
  display_products()
  prod_name=input("Enter the product Name:")
  i=0
  for product in products:
    if product[0].lower() == prod_name.lower():
      products[i][0]=input("Enter new Name:") or product[0]
      products[i][1]=float(input("Enter new Price:")) or product[1]
      products[i][2]=int(input("Enter new Quantity:")) or product[2]
      print("Product updated.")
      break
    i+=1
  else:
    print("Product not found.")
def delete_product():
  display_products()
  prod_name=input("Enter the product Name:")
  i=0
  for product in products:
    if product[0].lower() == prod_name.lower():
      del products[i]
      print("Product deleted.")
      break
    i+=1
  else:
    print("Product not found.")

