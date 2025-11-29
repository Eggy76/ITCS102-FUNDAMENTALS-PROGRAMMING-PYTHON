#while loop

bo = True

while bo == True:
    a = input("(Yes or No): ")

    if a.lower() == "yes":
        print("Continue")
        continue
    elif a.lower() == "no":
        print("Stop")
        break
    else:
        print("Error input")
        continue
