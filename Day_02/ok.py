#Mini Challenge: Student Grades Manager

d={}

while True:
    print("\n------ Student Grades Manager ------\n")
    print("1. Add Student\n2. View All Students\n3. Update Marks\n4. Delete Student\n5. Exit\n")

    s=int(input("Enter Your Choice: "))
    
    if s==1:
        add_name=input("Enter Student Name: ")
        enter_marks=int(input("Enter Marks: "))
        d.update({add_name:enter_marks})

    elif s==2:
        for key, value in d.items():
          print(f"{key}: {value}")

    elif s==3:
        add_name=input("Enter Student Name: ")
        enter_marks=int(input("Enter Marks: "))
        d.update({add_name:enter_marks})

    elif s==4:
        add_name=input("Enter Your Name: ")
        d.pop(add_name)
        print(f"{add_name} removed.")
    
    elif s==5:
        break

    else:
        print("You Enter Invalid")


