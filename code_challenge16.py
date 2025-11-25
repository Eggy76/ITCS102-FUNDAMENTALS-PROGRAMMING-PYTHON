
import os
import json
os.system('cls')
print("STUDENT INFORMATION SYSTEM ")
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
        os.system('cls')
        for a,r in student_records.items():
                print("The Records is Found ^_^* ")
        
                print("Record List")
                print("============================")
                print(f"STUDENTS ID {a}: STUDENT RECORD {r}") #it will now print all the items in dictionary
        continue

    elif choice == "c":
        code = input("Input the Student Code : ").lower()

        for a in student_records.keys():
            if code in student_records.keys():
                print("The Record is Found ^_^* ")
        
                print("\nRecords")
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

    elif choice == "e":
        print("Record Modification : ")
        code = input("Enter Student Key : ")
        for a in student_records[code]:
            print(f": {a}")

        first_name = input("Input Student First Name : ").upper()
        last_name = input("Input Student Last Name : ").upper()
        course = input("Input Student Course : ").upper()
        email = input("Input Student Email : ").upper()
        pogi = input("Input Student Pogi (Yes or No): ").upper()

        student_records[code][0] = first_name
        student_records[code][1] = last_name
        student_records[code][2] = course
        student_records[code][3] = email
        student_records[code][4] = pogi

        print("Data Updated! ")
        continue

    elif choice == "f":
        os.system('cls')
        with open("student_records.json","w") as new_file:  
            json.dump(student_records,new_file, indent=4)
            print("Data Exported")
            continue
    elif choice == "g":
        os.system('cls')
        with open("student_records.json","r") as new_file:
            student_records = json.load(new_file)

        student_records = student_records
        print("Data Imported")

        continue
    elif choice == "p":
        print("Exiting")
        break
   
    else:
        print("No Record Found. . . '^' ")
        continue


