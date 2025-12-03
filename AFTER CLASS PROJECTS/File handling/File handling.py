# FUNCTION DECLARING
def Reading():
    # READING
    thisfile = open("Sports.txt")
    print(thisfile.read())
    thisfile.close()

def Writing():
    # WRITING
    thisfile = open("Sports.txt","w")
    thisfile.write("Excercise more,achieve more. Play sports, achieve even more!")
    thisfile.close()


def Appending():
    # APPENDING
    thisfile = open("Sports.txt","a")
    thisfile.write("\n Why not just play sports instead of studying.")
    thisfile.close()

# FUNCTION IMPORTING
menu = 0
while menu<4:
    print("1. Read  \n2. Write \n3. Append \n4. Exit")
    menu = int(input("Pick from any of these 4 options: "))
    print("_________________________________________")

    if menu == 1:
        print("_________________________________________")
        print("Opening file in Read Mode. ")
        Reading()
        print("_________________________________________")
        
    

    if menu == 2:
        print("_________________________________________")
        print("Opening File in Write Mode. ")
        Writing()
        print("_________________________________________")

    if menu == 3:
        print("_________________________________________")
        print("Opening file in Append Mode. ")
        Appending()
        print("_________________________________________")

    if menu == 4:
        print("_________________________________________________________")
        print("Thanks for viewing dear user, have a great day ahead!")
        print("_________________________________________________________")