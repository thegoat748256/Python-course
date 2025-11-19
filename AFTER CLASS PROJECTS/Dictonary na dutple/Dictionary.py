my_dict = {}

my_dict = {1: "10",2: "20",3: "30",4: "40",5: "50",6: "60"}

number = int(input("Please enter a number between 1 and 6 "))

pos = my_dict.get(number)

print("According to my dictionary, the value in",number,"is",pos,"")