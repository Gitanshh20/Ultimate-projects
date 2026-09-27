# How to Find Area Using Heron's in Python

import math

print("Finding Area of Triangle Using Heron's Formula")

# Three Sides

a = float(input("Enter Your Side 1: "))
b = float(input("Enter Your Side 2: "))
c = float(input("Enter Your Side 3: "))

# Perimeter

Perimeter = a + b + c
print(f"Your Perimter: {Perimeter}")

# Semi-Perimeter

s = Perimeter/2
print(f"Your Semi-Perimeter: {s}")

# Area Of Triangle Using Heron's

Area = round(math.sqrt(s*(s-a)*(s-b)*(s-c)), 2)

print(f"Area of Triangle: {Area} sq unit")