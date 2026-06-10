# To-Do-list

task = []

while True:
    print("\n1.Add Task\n2.Delete Task\n3.View Task\n4.Exit\n")
    
    choice = input("Enter Your Choice: ")
    
    if choice =='Add Task' or choice == '1':   
        n = input("Enter Your Task: ")
        task.append(n)
        
    elif choice == 'Delete Task' or choice == '2':
        print(task)
        delete = int(input("Enter Number of Task: ")) - 1
        task.pop(delete)
        
    elif choice == 'View Task' or choice == '3':
        print('\nYour Tasks: ',task)
            
    elif choice == 'Exit' or choice == '4':
        break
    
    else:
        print("Something Went Wrong Try Again.....")