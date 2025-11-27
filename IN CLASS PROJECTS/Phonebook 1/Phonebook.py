# Module importing
import sys
def initial_phonebook():
     no_Contacts = int(input("Please enter the amount of contacts."))
     no_Details = 5

     phone_book = []
     print(phone_book)
     for i in range(no_Contacts):
          temp = []
          for j in range(no_Details):
               if j == 0:
                    temp.append(str(input("Please enter contact name. ")))
                    if temp [j] == " ":
                         sys.exit("Name is a mandatory field. Please try again.")

               if j == 1:
                    temp.append(int(input("Please enter contact number.")))
                    if temp [j] == " ":
                         sys.exit("Contact number is a mandatory field. Please try again.")

               if j == 2:
                    temp.append(str(input("Please enter email id.")))
                    if temp [j] == " ":
                         temp [j] = None

               if j == 3:
                    temp.append(str(input("Please enter date of birth (DOB).")))
                    if temp [j] == " ":
                         temp [j] = None

               if j == 4:
                    temp.append(str(input("Please enter category.")))
                    if temp [j] == " ":
                         temp [j] = None

          phone_book.append(temp)                                  
     print(phone_book)
     return phone_book

 #Welcome msg
print("____________________________________________________________________________")
print("Welcome to the phonebook.")
print("You may kindly proceed through our features.")
print("____________________________________________________________________________")

#Choices
ch = 1
pb = initial_phonebook()
while ch in (1,2,3,4,5):
    ch = menu()
    if ch == 1:
         pb = add_contact(pb)

    elif ch == 2:
         pb = remove_existing(pb)

    elif ch == 3:
         pb = delete_all(pb)

    elif ch == 4:
         d = search_existing(pb)
         if d == -1:
              print("There is no contact with this username, kindly please try again")

    elif ch == 5:
         display_all(pb)

    else:
         thanks()

def menu():
     print("_____________________________________________________________")
     print("You can now perform all of these actions:")
     print("1. Add a new contact.")
     print("2. Remove an existing contact.")
     print("3. delete all the contacts.")
     print("4. search for an existing contact.")
     print("5. display all contacts")
     print("6. exit/close the phonebook")
     print("_____________________________________________________________")