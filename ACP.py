def numberadd(a, b):
    return a + b

def numbersubtract(a, b):
    return a - b

def numbermultiply(a, b):
    return a * b

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("The sum of the two numbers is: " + str(numberadd(a, b)))
print("The difference of the two numbers is: " + str(numbersubtract(a, b)))
print("The product of the two numbers is: " + str(numbermultiply(a, b)))