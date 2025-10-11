

for outer in range(1,11,1):
    for kalso in range(10,outer,-1):
        print(" ",end=" ")
    for inner in range(0,outer,1):
        print("",end=" ")
    for inner in range(1,outer,1):
        print("*",end=" ")
    for kalso in range(10,outer,-1):
        print(" ",end=" ")
    print()
for outer in range(9,0,-1):
    for kalso in range(10,outer,-1): 
        print(" ",end=" ") 
    for inner in range(0,outer,1):
        print("",end=" ")
    for inner in range(1,outer,1):
        print("*",end=" ")
    for kalso in range(10,outer,-1):
        print(" ",end=" ")
    print()
