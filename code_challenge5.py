#manga introduction

#main menu of manga

#options of your manga

#title of you manga

print("Welcome to Manga Hub :>")

#1 Action

#2 Romance

#3 = Horror

print("Answer a few question before we proceed on type of manga's, Choose a number of your choice.")

print("What type of genre: ")

gen = int(input('\n1.Action\n2.Romance\n3.Horror\nAnswer:'))

if gen ==  1:

    print("Welcome to the list of Action Manga's ")
elif gen ==  2:
    print("Welcome to the list of Romance Manga's ")

elif gen ==  3:
    print("Welcome to the list of Horror Manga's ")

else:
    print("Sorry! We dont have that kind of Manga here. Try again!")

print("How long the manga should be? ")

dor = input("\n1.short\n2.medium\n3.long\nAnswer:")

if dor == "1":
    
    print("You chose short now lets proceed on decade's")

elif dor == "2":

    print("You chose medium now lets proceed on decade's")

elif dor == "3":
    
    print("You chose long now lets proceed on decade's")

else:
    print("Sorry! We dont have that kind of choices here. Try again! ")

print("What decade's it should be? ")

dec = input("\n1.2000s\n2.2010s\n3.2020s\nAnswer: ")

if dec == "1":
	
	print("You chose 2000s, Now Enjoy!")

elif dec == "2":

	print("You chose 2010s, Now Enjoy!")

elif dec == "3":

	print("You chose 2020s, Now Enjoy!")

else:
	print("Sorry! We dont have that kind of choices here. Try again! ")


print("Here's some recommendation for you during 2000s,2010s,2020s: ")
print("\nNaruto (1999–2014) – Masashi Kishimoto \nBleach (2001–2016) – Tite Kubo\nOne Piece (1997–present, huge in the 2000s) – Eiichiro Oda\nFullmetal\nAlchemist (2001–2010) – Hiromu Arakawa\nDeath Note (2003–2006) – Tsugumi Ohba & Takeshi Obata\nGantz (2000–2013) – Hiroya Oku\nD.Gray-man (2004–present) – Katsura Hoshino\nBlack Cat (2000–2004) – Kentaro Yabuki\nBuso Renkin (2003–2005) – Nobuhiro Watsuki\nEyeshield 21 (2002–2009) – Riichiro\nInagaki & Yusuke Murata")



