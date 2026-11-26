
# Multiple parameters

def calculate_total_price(price,quantity,discount):
    total=(price*quantity)-discount
  
    if discount>0:
        total-=discount

    print(f"Total price is {total}")   
   
quantity=int(input("Enter the quantity of your items: "))
price=int(input("Enter the item price: "))
discount=int(input("Enter the discount of your items: "))


calculate_total_price(price,quantity,discount)
