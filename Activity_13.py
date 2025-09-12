#loop 10x
#then get the summation of all the numbers

num = 1000
for x in range(1, 11):
  number = eval(input('enter a number to stand on a price: '))
  num -= number
  print('the result is', num)
  print('your remaining money is', num)
