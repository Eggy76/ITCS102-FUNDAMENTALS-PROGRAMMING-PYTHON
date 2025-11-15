

print("Adding Anime Data to Dictionary")
print("===============================")

bo = True

empty_dict = {}

def print_anime(): 
    for c,t in empty_dict.items():
        print(f"Code -- {c}  Title -- {t}")

def search_list(key):
    print("Searching. . .")
    print(f"Result. . .{empty_dict[key].upper()}")

while bo == True:
    keys = input("Input Keys for Anime : ")
    value = input("Enter Anime Title : ")
#inputting key and valaues for users anime input

    empty_dict[keys] = value #adding data to dictionary

    choice = input("Would you like to Continue adding more anime? :> \nY - Yes \nN - No \nP - Print \nS - Search \nChoice : ").lower()

    if choice == "y":
        print("Continuing. . .")
        continue
    elif choice == "n":
        print("Program stop. . .")
        break
    elif choice == "p":
        print("Here's the list of your anime")
        print_anime()
        continue
    elif choice == "s":
        code = input("Input the Code of Anime : ")
        search_list(code)
        continue
    else:
        print("Invalid Choice!!!. . .")
        continue
