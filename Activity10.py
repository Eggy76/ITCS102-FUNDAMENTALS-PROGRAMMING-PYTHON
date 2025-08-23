#name
#student or not
#fare or bayad
#discount

passenger = input("Input your name: ")
passenger1 = input("Are you a student (yes / no): ")
fare = eval(input("Pay: "))

if passenger1.lower() == "yes" :
	discount = fare * .16
	new_fare = fare - 2.0
	print("Congrats discount has been approved your newfare is",new_fare,  "Enjoy your ride with us")
else:
	print("Sorry your request on the discount has not been approved")
	
