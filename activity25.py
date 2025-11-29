from activity25_1 import activity1, activity2, activity3, activity4

name  = input("Whats is your name : ")

print(f"Welcome {name} to my File Compiler")

bo = True

while bo == True:
    print("Select a program")
    print("A - Activity1\nB - Activity2\nC - Activity3\nD - Activigty 4\nE - Exit")

    choice = input("What program would you like to run: ").lower()

    if choice == "a":
        activity1()
        continue
    elif choice == "b":
        activity2()
        continue
    elif choice == "c":
        activity3()
        continue
    elif choice == "d":
        activity4()
    elif choice == "e":
        print("Thank you! ")
        break
    else:
        print("choice is not available!")
