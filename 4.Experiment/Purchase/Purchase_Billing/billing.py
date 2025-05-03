from Product_Details.entry_display import products, display_products

def adding_product():
  cart=[]
  amount=0
  tax=0.18
  discount=0
  display_products()
  while True:
    prod_name=input("Enter product Name(0 for billing):")
    if prod_name=='0':
      break
    for product in products:
      if product[0].lower() == prod_name.lower():
        quantity=int(input("Enter the quantity:"))
        if quantity<=product[2]:
          cart.append([product[0],product[1],quantity])
          amount+=quantity*product[1]
          product[2]-=quantity

          break
        else:
          print(f"Only {product[2]} of {product[0]} available")
          break
    else:
      print("Product not found.")    
  '''Billing the added products'''
  if len(cart)==0:
    print("No product added")
    return
  print("\n_____Billing_____\n")
  if amount>1000:
    discount=0.1*amount
    print(f"You got 10% ₹{discount} Dicsount.")
  discount_amount=amount-discount
  tax_amount=tax*discount_amount
  final=discount_amount+tax_amount
  print("Your cart products are:")
  i=0
  print("S.No\tName\tPrice\tQuantity")
  for product in cart:
    print(f"{i+1}.\t{product[0]}\t{product[1]}\t{product[2]}")
    i+=1
  print("Sub total\t:%.2f"%amount)
  print("Tax amount\t:%.2f"%tax_amount)
  print("Final amount\t:%.2f"%final)
