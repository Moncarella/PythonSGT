name1 = input("Enter the name:\n")
lastname1 = input("Enter the last name:\n")

name2 = input("Enter the name:\n")
lastname2 = input("Enter the last name:\n")

name3 = input("Enter the name:\n")
lastname3 = input("Enter the last name:\n")

name4 = input("Enter the name:\n")
lastname4 = input("Enter the last name:\n")

# Instead of repeating the same code several times, we can create a function:
def enterNameLastName():  # def means you define function name
    name = input("Enter the name:\n")
    lastName = input("Enter the last name:\n")
    return name, lastName



name1, lastname1 = enterNameLastName()
name2, lastname2 = enterNameLastName()
name3, lastname3 = enterNameLastName()
name4, lastname4 = enterNameLastName()

def printFullName(name, lastName):
    print(name + " " + lastName)

def getMiddleElement(l:list):  # if you specify the type here, the options for lists will appear below
    length = len(l)
    if length == 0:
        return None
    elif length == 1:
        return l[0]
    else:
        middlePoint = int(length / 2)
        if length % 2 == 1:
            return l[middlePoint]
        else: return l[middlePoint-1], l[middlePoint + 1] # indexes start at 0
# If we were to add [] everywhere, the function would return a list

print(getMiddleElement([1,5,3,6,4,7]))
print(getMiddleElement([1,5,4,7]))

def actions(*args):   # If you don't know how many arguments
    for arg in args:
        print(arg)

actions(5,4,2,6,7)

# You can also build a dictionary function to provide key and value pairs
def actionsKW (**kwar):
    print(kwar)
    for key in kwar:
        print(str(key) + " : " + str(kwar.get(key)))

actionsKW(Name = "Arturs", LastName = "Olekss")


def calculatePerimeter(a,b):
    return 2 * (a + b)

print(calculatePerimeter(2,8))

def calculatePerimeter(a,b,c):
    return a + b + c

print(calculatePerimeter(2,8,6))
# the later code rewrites the function, so the latest function works

# Shorter way for defining the functions: Lambda functions
sqr = lambda x : x * x
print(sqr(4))