sum = 0
sumOdd = 0
sumEven = 0
for i in range(0,10):
   number = eval(input("Enter your number : "))
   sum += number
        
   if number % 2 == 0:
      sumEven += number
   else:
      sumOdd += number
print(f"The sum of all numbers are : {sum}")
print(f"The sum of all odd numbers are : {sumOdd}")
