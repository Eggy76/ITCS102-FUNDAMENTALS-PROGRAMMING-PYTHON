

for i in range(11,0,-1):
  for x in range(1, i, 1):
    print(" ", end= ' ')
  for y in range(10, i, -1):
    print("*",end = ' ')
  for i in range(10,i,-1):
    print("*",end = ' ') 
  print()
