amount = int(input("Enter amount to deposit: "))

a = amount // 1000
amount = amount % 1000

b = amount // 500
amount = amount % 500

c = amount // 200
amount = amount % 200

d = amount // 100
amount = amount % 100

e = amount // 50
amount = amount % 50

f = amount // 20
amount = amount % 20

g = amount // 10
amount = amount % 10

h = amount // 5
amount = amount % 5

i = amount // 1
amount = amount % 1

print("P1000:", a)
print("P500 :", b)
print("P200 :", c)
print("P100 :", d)
print("P50  :", e)
print("P20  :", f)
print("P10  :", g)
print("P5   :", h)
print("P1   :", i)