def addition(x, y):
    total = x + y
    return total
def subtraction(x, y):
    total = x - y
    return total
def multiplication(x, y):
    total = x * y
    return total
def division(x, y):
    total = x / y
    return total

number1 = float(input("what is your first number: "))
number2 = float(input("what is your second number: "))
operation = input("what operation would you like to do: ")
if operation == "+":
    print("your number is")
    print(addition(number1, number2))
    print("Dont know why you asked me to do your math lazy.")
if operation == "-":
    print("your number is")
    print(subtraction(number1, number2))
    print("Dont know why you asked me to do your math lazy.")
if operation == "*":
    print("your number is")
    print(multiplication(number1, number2))
    print("Dont know why you asked me to do your math lazy.")
if operation == "/":
    if number1 == "0" or number2 == "0":
        print("You really flunked out of the 2nd grade didn't you. That is IMPOSSIBLE stupid.")
    elif not number1 == "0" or number2 == "0":
            print("your number is")
            print(division(number1, number2))
            print("Dont know why you asked me to do your math lazy.")