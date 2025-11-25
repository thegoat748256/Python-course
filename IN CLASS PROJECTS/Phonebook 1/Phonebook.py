# Module importing
import sys
def initial_phonebook():
     rows, cols = int(input("Please enter the amount of contacts.")),5

     phone_book = []
     print(phone_book)
     for i in range
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
         delete_all(pb)

    else:
         thanks()