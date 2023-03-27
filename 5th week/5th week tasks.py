# Task 1
# Write a function that takes two parameters (a and b) and returns their sum

def calcSum():
    a = int(input("Enter the first number:\n"))
    b = int(input("Enter the second number:\n"))
    return a + b

print("The sum equals: ", calcSum())


# Task 2
# Write a function that takes a string as a parameter and returns the number of vowels (aeiou) in the string. Hint: you can use given_character in "aeiou"

def countVowels(str):
    count = 0
    vowels = set("aeiou")
    for letter in str:
        if letter in vowels:
            count += 1
    
    print("Number of vowels in given text:", count)

str = str(input("Enter text:\n"))
countVowels(str)


# Task 3
# Write a function that takes a string as a parameter and returns True if the string is a palindrome and False otherwise

def ispalindrome(str):
    if str == str[::-1]:
        return print("True")
    else:
        return print("False")

str = str(input("Enter word:\n"))
ispalindrome(str)


# Task 4
# Write a function that takes a list of integers as a parameter and returns a list of only the even integers in the original list

def evenInt (l:list):
    newlist = []
    for integer in l:
        if (integer % 2) == 0:
            newlist.append(integer)
        else:
            continue
    return print(newlist)

evenInt([1,2,3,4,5,6])
evenInt([10,15,17,22,43])


# Task 5
# Write a function that takes a list of integers and a target sum as parameters and returns a list of two integers from the original list that add up to the target sum

def intTargetSum (l:list, targetSum:int) -> list:
    for i in l:
        for j in l:
            if (i + j) == targetSum:
                listForSum = [i, j]         
            else:
                continue
    return print("Integers", listForSum, "add up to the target sum of", targetSum)

intTargetSum([5,10,23,4,7,17], 24)


# Task 6
# Write a function that takes a list of integers as a parameter and returns the product of all the integers in the list

def intProduct (l:list):
    res = 1
    for i in l:
        res = res * i
    return print("The product of all the integers in the list is:", res)

intProduct([1,2,3])


# Task 7
# Write a function that takes a dictionary as a parameter and returns a list of all the keys in the dictionary that have an even value

def dictEvenVals (dict):
    keyList = []
    for keys, values in dict.items():
        if values % 2 == 0:
            keyList.append(keys)
    return print(keyList)

dictEvenVals({"args1":6, "args2":10, "args3":7})

# Task 8
# Write a function that takes a list of dictionaries as a parameter and returns a new dictionary that contains the sum of the values for each key in the original dictionaries

def sumOfKeys(dictList:list):
    sum_dict = dict()
    for values_dict in dictList:
        for key, value in values_dict.items():
            if key in sum_dict:
                sum = sum_dict.get(key)
                sum += value
                sum_dict[key] = sum
            else: sum_dict[key] = value
    return sum_dict

dictInput = [{1:20, 2:9, 3:15}, {1:30, 2:8, 3:13}, {1:23, 2:1, 3:7}]
print(sumOfKeys(dictInput))

# Task 9
# Write a function that takes a tuple as a parameter and returns a new tuple that has the first and last elements swapped

def elSwapped(tuple1:tuple):
    tuple1_list = list(tuple1)
    tuple1_list[0], tuple1_list[len(tuple1_list)-1] = tuple1_list[len(tuple1_list)-1], tuple1_list[0]
    return tuple(tuple1_list)

tupleInput = (34,24,65,3453,1,234,8)
print(elSwapped(tupleInput))

# Task 10
# Write a function that takes a set as a parameter and returns a new set that contains only the elements that are not divisible by 3

def notDivisibleSet(set1:set):
    newset = set()
    for element in set1:
        if element % 3 == 0:
            continue
        else: newset.add(element)
    return newset

setInput = {1,3,5,7,12,13,26,30}
print(notDivisibleSet(setInput))
