def is_disarium(number):
    num_str = str(number)
    length = len(num_str)
    total = 0
    for i in range(length):
        total = total + int(num_str[i]) ** (i + 1)
    if total == number:
        print(number,"is a Disarium number.")
    else:        
        print(number,"is not a Disarium number.")
number = int(input("Please enter a number: "))
is_disarium(number)