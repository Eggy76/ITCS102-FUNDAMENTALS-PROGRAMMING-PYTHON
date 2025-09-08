

temp = eval(input("Enter the Temperature: "))

if temp <= 0:
	print("Temperature outside is freezing cold")
elif temp >= 1 and temp <= 20:
	print("Temperature outside cold")
elif temp >= 21 and temp <30:
	print("Temperature outside lukewarm")
elif temp >= 31 and temp <= 40:
	print("Temperature outside warm")
elif temp >= 41 and temp <= 50:
	print("Temperature outside above boiling hot")
elif temp >= 51:
	print("Temperature outside above boiling hot")
else:
	print("invalid temperature")
