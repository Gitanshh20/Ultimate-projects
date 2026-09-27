# How to Find Distance in Python ?

import math

x1 = float(input("Enter Your x1-co: "))
x2 = float(input("Enter Your x2-co: "))
y1 = float(input("Enter Your y1-co: "))
y2 = float(input("Enter Your y2-co: "))

distance = round(math.sqrt(((x2 - x1)** 2) + ((y2 - y1)** 2)), 2)

print(f"Here Your Distance: {distance} units")