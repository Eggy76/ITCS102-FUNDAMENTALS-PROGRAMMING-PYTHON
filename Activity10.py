#name
#student or not
#fare or bayad
#discount

passenger = input("Input your name: ")
passenger1 = input("Are you a student (Yes / No): ")
fare = eval(input("Pay: "))

if passenger == "yes" :
	discount = fare * .15
	new_fare = fare - .15
	print("Congrats discount has been approved your newfare is",new_fare,  "Enjoy your ride with us")
else:
	print("Sorry your request on the discount has not been approved")
