print("Factorial")

Num = eval(input("Input a number: "))

result = 1
for x in range(Num, 0, -1):
    result *= x
       
    print("Factorial is", result) 
