import random
import sys

Choice = input("Hey there! do you want to roll a dice? type yes or no. ")

while Choice == "yes":
    if Choice == "yes":
        RN = random.randint(1,6)
        dice_result = print("You have rolled a ",RN)

    ch = input("Do you want to roll again? type yes or no. ")
    if ch == "yes":
        RN
    if ch == "no":
        sys.exit("Ok, have a great day ahead! ")
if Choice == "no":
    sys.exit("Ok, have a great day ahead! ")