import os 

file = input("Enter Your File Path: ")

with open(file, 'r') as f:
    if 'Binod' in f.read():
        print("Binod Find!!!")
    
    else:
        print("Binod Didn't Find..")