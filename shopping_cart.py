def add_items(item_name,price,cart):
   cart[item_name]=price         #create a cart dictionary to store item name and price
   print(f"Item {item_name} added to cart for the {price}")
def total_price(cart):
    s=0
    for name,price in cart.items():
      s+=price
    return s
def view(cart):
    return cart
def main(): 
  cart = {}
  while True:
    print("\nShopping Cart Menu:")
    print("1. Add item to cart")
    print("2. View cart items")
    print("3. Calculate total price")
    print("4. Exit")
    choice = input("Enter your choice: ")         # Get user choice
    if choice=="1":
      item_name=input("Enter item name: ")
      price=int(input("Enter item price: "))
      add_items(item_name,price,cart)
    elif choice=="2":
      print(view(cart))
    elif choice=="3":
      print(f"Total price: {total_price(cart)}")
    elif choice=="4":
      break
    else:
      print("Invalid choice. Please choose a valid option.")           # Handle invalid choice
main()
      

