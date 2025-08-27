#username
#pass
#login
#access granted

from getpass import getpass
username = 'christian'
password = 'pogiako159'

name = input("Username: ")
if name.lower() == "christian":
	print("Access Granted ")
else:
	print("Access Denied ")
pword = getpass("Password: ")
if pword.lower() == "pogiako159":
	print("Access Granted")
else:
	print("Access Denied")
