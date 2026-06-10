# Receipt Generator

prices = []

while True:
    try:
        price = float(input("Enter Price Here or Press 0 for Quit: "))
        prices.append(price)
        
        if price == 0:
            break
        
    except ValueError:
        print("Enter a vaild Number")
    
total = sum(prices)

print(f"\nYour bill is: ₹{total}")
  
