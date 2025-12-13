import sys
def Add_nums(numbers):
    ans = 0
    for i in range(len(numbers)):
        ans = ans + numbers[i]
    print(ans)

def Subtract_nums(numbers):
    ans = numbers[0]
    for i in range(1,len(numbers)):
        ans = ans - numbers[i]
    print("The answer is: ",ans)

def Multiply_nums(numbers):
    ans = 1
    for i in range(len(numbers)):
        ans = ans * numbers[i]
    print("The answer is: ",ans)
    
def Divide_nums(numbers):
    ans = numbers[0]
    for i in range(1,len(numbers)):
        ans = ans / numbers[i]
    print("The answer is: ",ans)

def Thanks():
    print("Thank you for using this calculator. Have a great day ahead!")
    sys.exit("Have a great day ahead. ")

choice = 1
while choice in (1,2,3,4,5):
    choice = int(input("Choose from one of these five, Then, type the corresponding number based on the list. \n 1. add\n 2. subtract\n 3. multiply\n 4. divide\n5. exit\n Choose a number "))

    if choice  == 5:
        Thanks()
    temp = 0
    numbers = []
    while temp >= 0:
        temp =  int(input("Enter a number. Enter -1 to quit. "))
        if temp >= 0:
            numbers.append(temp)
    print("Number of terms you have entered: ",len(numbers))
    
    if choice == 1:
        Add_nums(numbers)

    if choice == 2:
        Subtract_nums(numbers)

    if choice == 3:
        Multiply_nums(numbers)

    if choice == 4:
        Divide_nums(numbers)