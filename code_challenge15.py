#Anime list
#Using list and while loop
print("Anime Title List")

anime = [] #empty list
bo = True   

while bo == True:
    name = input("Put a Title of an Anime: ")
    print("Anime Added to the your Anime List")
    anime.append(name) #all title that put will go to the list
    if name == "exit": #stopper
        print("All done,You are now exiting!! ")
        anime.pop() #will remove the string exit to list
        break    #to stop the loop

print(f"Here All the Title of your Anime: ") 
for a in anime:     #will print all the anime u putted,from up to down
    print(f"- {a}")
