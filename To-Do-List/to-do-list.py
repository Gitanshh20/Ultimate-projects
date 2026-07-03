# To-Do list 

print("To-Do-List | Code by Gitansh")

def ToDoList():
    tasks = []
    
    while True:
        print("1.Add Tasks")
        print("2.View Tasks")
        print("3.Delete Tasks")
        print("4.Exit")
        
        choice = int(input("\nEnter Your Choice: "))
        
        if choice == 1 :
            NoOfTask = int(input("Enter Number of Task You Want to Add: "))
            for task in range(1, NoOfTask + 1):
                task = input("Enter Your Task: ")
                tasks.append(task)
            print("Your All Task Added.")
            
        elif choice == 2:
            if tasks == []:
                print("No Task found...\n")
            else:        
                print(f"Here Your All Task -> {tasks}\n")
            
        elif choice == 3:
            if tasks == []:
                print("No Data Found..")
            else:
                print(f'Here Your Tasks -> {tasks}\n')
                indexOfTask = int(input("Enter Number of Task You Want to delete: ")) - 1
                tasks.pop(indexOfTask)
                print('Your Task is Deleted.')
                
        elif choice == 4:
            print("GoodBye!!")
            break            
            
if __name__ == '__main__':
    ToDoList()
