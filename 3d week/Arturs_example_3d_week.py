# Task 1

number = int(input("Enter an integer number: "))
if number == 0:
    print("Number is zero")
elif number > 0:
    print("Number is positive")
else:
    print("Number is negative")


# Task 2
Same solution, but if we have a much wider range, we could 
use flag variables to make the solution use less computational resources:

for i in range(1,101):
    
    printnumber = True
    if i % 3 == 0:
        print("Fizz", end="")
        printnumber = False

    if i % 5 == 0:
        print("Buzz", end="")
        printnumber = False
    
    if printnumber:
        print(i)
    else: # go to the next line
        print()


# Task 3 - added solution for negative numbers
number = int(input("Please enter number\n"))

if number < 0:
    print(-1)
    for i in range(-2, number, -1):
        if number % i == 0:
            print(i)
    print(number)
elif number > 0:
    print(i)
    for i in range(2, number):
        if(number % i == 0):
            print(i)
    print(number)
else: #0
    print("All the numbers")


# Task 4
number1 = float(input("Enter number 1"))
number2 = float(input("Enter number 2"))

while True:
    operation = input("Enter operation (*, /, +, - or %)")
    if operation == "*":
        result = number1 * number2
    elif operation == "/":
        result = number1 / number2
    elif operation = "+":
        result = number1 + number2
    elif operation == "-":
        result = number1 - number2
    elif operation == "%":
        result = number1 % number2
    else:
        print("Operator is not correct")
        continue
    print("Result is" + str(result))
    break


# Task 5
numberUp = int(input("Enter the number\n"))

for number in range(2, numberUp+1):
    prime = True

    for i in range(2,number):
        if(number % i == 0):
            prime = False
    
    if number > 1 and prime:
        print(number)