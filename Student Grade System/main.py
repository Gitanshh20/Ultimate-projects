# Student Grade System.. 

print("Student Grade System | Code by Gitansh")

student_grade = []
    
while True:
    print("\n1.Add Student")
    print("2.View Student")
    print("3.Delete Student")
    print("4.Exit")
    
    choice = input("\nEnter Your Choice: ")
    
    if choice == '1' or choice == 'Add Student':
        name = input("\nEnter Student Name: ")
        grade = input(f"Enter Grade of {name}: ")
        student_grade.append(name+':' +grade)
        
    elif choice == '2' or choice == 'View Student':
        if student_grade == []:
            print("\nNo Data Found")
        else:
            print('View Student Data:',student_grade)
        
    elif choice == '3' or choice == 'Delete Student':
        print('View Student Data:',student_grade)
        delete = int(input("Enter Number for Delete: ")) - 1
        student_grade.pop(delete)
        
       
    elif choice == '4' or choice == 'Exit':
        print("GoodBye!")
        break
    
    else:
        print('Try Again. Something Went Wrong')