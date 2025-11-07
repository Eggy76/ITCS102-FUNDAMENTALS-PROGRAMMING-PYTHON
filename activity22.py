#Guess the number

import random

print("gi hula ko ug imong number")

ran_number = random.randint(1,5)
tries = 0
a = True

while a == True:
    num = int(input("Mag lagay ng imong number : "))

    tries += 1

    if num == ran_number:
        print("You Guess The right number ! ")
        print(f"Only took {tries} tries")
        break
    else:
        print("No you're wrong!")
        print('Continue')
        continue


