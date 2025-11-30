#sys module importing
import sys

def initial_Slambook():
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
                    