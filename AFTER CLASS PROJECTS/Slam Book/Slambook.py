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
    for i in range (len(sb[0])):
        if i == 0:
            Dip.append (str(input("Enter friend's name. ")))

        if i == 1:
            Dip.append (int(input("Enter friend's contact number. ")))

        if i == 2:
            Dip.append (str(input("Enter friend's nickname. ")))

        if i == 3:
            Dip.append (str(input("Enter friend's message about you. ")))

        if i == 4:
            Dip.append (str(input("Enter friend's date of birth (DOB) dd/mm/yyyy. ")))
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
    confirm =  str(input("Do you want to delete all friends? You cannot retrieve your friends back. Type N or Y. "))
    if confirm in("Y","y"):
        print("All friends are deleted. ")
        return sb.clear()
    elif confirm in("N","n"):
          print("No friends deleted. ")
          return sb
    else:
          print("This is not valid. Try again. ")
    

def search_existing(sb):
     temp = []
     check = -1
     choice = int(input("Enter search criteria 1. Name. 2. Number 3. Nickname 4. Message 5. DOB. Please enter: "))

     if choice == 1:
          query = str(input("Enter friend's name. "))
          for i in range(len(sb)):
               if query == sb[i][0]:
                    check = 1
                    temp.append(sb[i])

     elif choice == 2:
          query = int(input("Enter friend's number. "))
          for i in range(len(sb)):
               if query == sb[i][1]:
                    check = 1
                    temp.append(sb[i])

     elif choice == 3:
          query = str(input("Enter friend's nickname. "))
          for i in range(len(sb)):
               if query == sb[i][2]:
                    check = 1
                    temp.append(sb[i])
    
     elif choice == 4:
          query = str(input("Enter friend's message about you. "))
          for i in range(len(sb)):
               if query == sb[i][4]:
                    check = 1
                    temp.append(sb[i])
    
     elif choice == 5:
          query = str(input("Enter friend's date of birth (DOB) dd/mm/yyyy. "))
          for i in range(len(sb)):
               if query == sb[i][3]:
                    check = 1
                    temp.append(sb[i])    

     else:
          print("Invalid search criteria. Try again. ")
          return -1

     if check == -1:
          return -1

     else:
          display_all(temp)
          return check


def display_all(sb): 
	if not sb: 
		print("List is empty: []") 
	else: 
		for i in range(len(sb)): 
			print(sb[i])


def thanks():
     print("___________________________________________________________________")
     print("Thank you for trying out this slambook system. ")
     print("Please visit again! ")
     print("___________________________________________________________________")
     sys.exit("Have a great day ahead!")


#main function
print("**********************************************************")
print("Welcome to the slambook. ")
print("Proceed further to explore. ")
print("**********************************************************")



#Choices (1,2,3,4,5)
ch = 1
sb = isb()
while ch in (1,2,3,4,5):
    ch = options()
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
         thanks()