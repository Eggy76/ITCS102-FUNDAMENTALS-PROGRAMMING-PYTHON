
import os

os.system('cls')
print("STUDENT INFORMSTION SYSTEM ")
print("===================================")

student_records = {}

while True:
    print("Select from the Option below : \nA - Add Student Record\nB - Print all Record\nC - Search a Student Record\nD - Delete a Record\nE - Edit Student Record\nF - Export Record\nG - Exit")

    choice =input("Choice : ").lower()

    if choice == "a":
        print("Adding a Student Information. . . .")
        print("====================================")
        search_code =input("Key name : ")
        
        first_name = input("Input Student First Name : ").upper()
        last_name = input("Input Student Last Name : ").upper()
        course = input("Input Student Course : ").upper()
        email = input("Input Student Email : ").upper()
        pogi = input("Input Student Pogi (Yes or No): ").upper()

        student_records = {search_code : [first_name, last_name, course, email, pogi ] }
        print("Data Saved. . . .")

        os.system("cls")
        continue
    elif choice == "b":
        code = input("Input the Student Code : ").lower()

        for a in student_records.keys():
            if code in student_records.keys():
                print("The Record is Found ^_^* ")
        
                print("Records")
                print("============================")

                for b in student_records[code]:
                    print(b)

    elif choice == "c":
        code = input("Input the Student Code : ").lower()

        for a in student_records.keys():
            if code in student_records.keys():
                print("The Record is Found ^_^* ")
        
                print("Records")
                print("============================")

                for c in student_records[code]:
                    print(c)
    elif choice == "d":
        print("Search Student : ")
        
        search_id = input("Input Student ID : ").lower()
    
        for id in student_records.keys():
            if search_id in student_records.keys():
                print("Students ID Found! ^-^* ")
                for a in student_records[search_id]:
                    print(f"  {a}")
                student_records.pop(search_id)

    elif choice == "d":
        print("Input a Student key to remove or delete : ")
        pass
    else:
        print("No Record Found. . . '^' ")
        continue
