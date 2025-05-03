products=[]
def add_product():
  products.append([input("Enter product name:"),float(input("Enter product price:")),int(input("Enter product quantity:"))])
  print("Product added successfully")
def display_products():
  if len(products)==0:
    print("No product available.")
    return
  i=0
  print("S.No\tName\tPrice\tQuantity")
  for product in products:
    print(f"{i+1}.",product[0],product[1],product[2],sep='\t')
    i+=1
