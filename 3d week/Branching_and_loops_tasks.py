# Task 1
# Write a program that takes a user input (an integer) and determines whether it is positive, negative, or zero.

number = int(input("Please enter a number: "))
if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
else:
    print("Number is zero")


# Task 2
# Write a program that prints out the numbers from 1 to 100. But for multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz". 
# For numbers that are multiples of both three and five, print "FizzBuzz".

for i in range(1,100):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else: print(i)

# Task 3
# Write a program that takes an integer as input and prints out all the factors of that integer.

print("Find out all the factors of the number")
number = int(input("Please enter number: "))

for i in range(1, number + 1):
    if number % i == 0:
        print(i)

# Task 4
# Create calculator: Ask user to provide 2 numbers and one operation to be performed (*,/,+.- or %). 
# If the operation provided does not match one of these, the program should print "Operation provided isn't valid, please,try again" - 
# in this case, the program should ask for the operation to be provided again

number1 = int(input("Please provide the first number: "))
number2 = int(input("Please provide the second number: "))
op = input("Please provide the operation you want to perform: ")
av_ops = ["*","/","+","-","%"]

while op not in av_ops:
    op = input("Operation provided isn't valid, please,try again: ")

print("The result is: ")
if op == "*":
    print(number1*number2)

elif op == "/":
    print(number1/number2)

elif op == "+":
    print(number1+number2)

elif op == "-":
    print(number1-number2)

elif op == "%":
    print(number1%number2)


# Task 5
# Write a program that takes an integer as input and prints out whether that integer is prime or not:

print("Find out if the number is prime")
number = int(input("Please enter the number: "))
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print("The number entered is not prime")
            break
    else: print("The number you entered is a prime number")
else: print("The number entered is not prime")

    
    



