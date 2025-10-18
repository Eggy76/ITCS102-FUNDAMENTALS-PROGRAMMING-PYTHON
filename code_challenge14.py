

name = input("Input your name : ")

odd = 0
num = "" 
angloop = True

while angloop == True:
    num = eval(input("input a number : "))
    if num % 2 == 1:
        print("Odd number")
        odd += num
        num += str(num) + "," 
        continue
    elif num == 0: 
        break
    else:
        print("Even")
        continue
print(f"Odd total number is: {odd}")
print(f"Odd number: {num}")
