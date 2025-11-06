def ADD(num1, num2):
    return num1 + num2

def MULTIPLY(num3, num4):
    return num3 * num4

def SUBTRACT(num5, num6):
    return num5 - num6

def DIVIDE(num6, num7):
    return num6 / num7

number = int(input("Enter a number "))

number2 = int(input("Enter another number "))
print("The sum is" ,(ADD(number,number2)))

print("The product is" ,(MULTIPLY(number,number2)))

print("The difference is" ,(SUBTRACT(number,number2)))

print("The quotient is" ,(DIVIDE(number,number2)))