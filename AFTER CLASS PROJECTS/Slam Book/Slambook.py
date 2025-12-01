#sys module importing
import sys

def isb():
    no_friends = int(input("Enter the number of friends. "))
    no_details = 5

    slambook = []
    print(slambook)
    for i in range (no_friends):
        tempo = []
        for j in range (no_details):
            if j == 0:
                tempo.append(str(input("Enter friend's name. ")))
                if tempo[j] == "":
                    sys.exit("Name is mandatory. Please try again. ")

            if j == 1:
                tempo.append(int(input("Enter friend's contact number. ")))
                if tempo[j] == "":
                    sys.exit("Number is mandatory. Please try again. ")

            if j == 2:
                tempo.append(str(input("Enter friend's nickname. ")))
                if tempo[j] == "":
                    tempo[j] = None

            if j == 3:
                tempo.append(str(input("Enter friend's message about you. ")))
                if tempo[j] == "":
                    tempo[j] = None

            if j == 4:
                tempo.append(str(input("Enter friend's date of birth (DOB). ")))
                if tempo[j] == "":
                    tempo[j] = None
        slambook.append(tempo)
    print(slambook)
    return slambook

def options():
    print("***************************************************************************")
    print("You can now perform these following actions: ")
    print("1. Add a friend. ")
    print("2. Delete a friend. ")
    print("3. Delete ALL friends. ")
    print("4. Search for an existing friend. ")
    print("5. Show all friends. ")
    print("6. Exit/close this slambook. ")
    print("***************************************************************************")
    choice = int(input("Enter choice number 1-6: "))
    return choice

def Add_friend(sb):
    Dip = []
    for i in range (len(sb)):
        if i == 0:
            Dip.append (str(input("Enter friend's name. ")))

        if i == 1:
            Dip.append (int(input("Enter friend's contact number. ")))

        if i == 2:
            Dip.append (str(input("Enter friend's nickname. ")))

        if i == 3:
            Dip.append (str(input("Enter friend's message about you. ")))

        if i == 4:
            Dip.append (int(input("Enter friend's date of birth (DOB) dd/mm/yyyy. ")))
    sb.append(Dip)
    return sb

def delete_friend(sb):
        remove = str(input("Enter the name of the friend you want to remove. "))
        tempoo = 0
        for i in range (len(sb)):
            if remove == sb[i][0]:
                tempoo = tempoo + 1
                print(sb.pop(i))
                print("This friend has been removed. ")
                return sb
        if tempoo == 0:
            print("This friend does not exist and we are not able to remove this friend. Try again or exit. ")
            return sb

def delete_all(sb):
    print("All friends are deleted. ")
    return sb.clear()


#main function
print("**********************************************************")
print("Welcome to the slambook. ")
print("Proceed further to explore. ")
print("**********************************************************")



#Choices (1,2,3,4,5)
ch = 1
sb = initial_slambook()
while ch in (1,2,3,4,5):
    ch = menu()
    if ch == 1:
         sb = Add_friend(sb)

    elif ch == 2:
         sb = delete_friend(sb)

    elif ch == 3:
         sb = delete_all(sb)

    elif ch == 4:
         d = search_existing(sb)
         if d == -1:
              print("No such friend exists. Try again. ")

    elif ch == 5:
         display_all(sb)

    else:
         thanks(sb)