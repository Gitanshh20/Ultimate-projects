# Digital Libaray System
import os

print("======================")
print("Digital Libaray System")
print("======================")

def Lib_System():
    while True:
        
        # Choices 
        print("1.Add Books\n2.Search Books\n3.Check Data\n4.Delete Data\n5.Exit")
        choice = int(input("Enter Your Choice: "))
        
        if choice == 1:
            Id = int(input("Enter Your ID: ")) # Id Number
            Qty = int(input("Enter Your Qty no. of Books: ")) # Quantity
            BookName = input("Enter Your Book Name(Search Books): ") # Book Name
            # File will created in Folder
            with open(f"Digital Libaray System\\{Id}.txt", "a") as f:
                f.write(f'ID No: {Id}\nQauntity: {Qty}\nBook: {BookName}')
            print("Your ID is Created and Your Book is Added\n")            
            
        elif choice == 2:
            # Books Name
            print("Top 5 Books ->\n-----------")
            print("1.Psychology of Money")
            print("2.Python Basics")
            print("3.C++ Core")
            print("4.Head of Java")
            print("5.Code Complete\n-----------")
            
        elif choice == 3:
            Entry = input("Are Created ID ? Yes/No: ") # Checking ID is Created or not
            if Entry == "No":
                print("Sorry!, First You Create the ID, Then You can Check.")
                
            elif Entry == "Yes":
                ID = int(input("Enter Your ID: "))
                with open(f'Digital Libaray System\\{ID}.txt', "r") as f: # Print the Status of Already Existing ID
                    Content = f.read()
                    print(f"Status of {ID} ->\n----------")
                    print(Content)
                    print("----------")
                    
            else:
                print("Invalid Option!!")
                
        elif choice == 4:
               Id = int(input("Enter Your ID: "))
               if os.path.exists(f"Digital Libaray System\\{Id}.txt"): # It will Delete Existing ID
                   os.remove(f"Digital Libaray System\\{Id}.txt")
                   print("Your ID is Deleted.")
               else:
                   print("No, Such ID Found!")
                   
        elif choice == 5:
            print("Thank You! For Visting.")
            break
        
        else:
            print("Sorry, We didn't Catch Try Again.")
            
if __name__ == "__main__":
    Lib_System()