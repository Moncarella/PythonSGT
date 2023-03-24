# listInt = [1,2,3,4,5]

# for element in listInt:
#     print(element)

# fruits = ["apple", "banana", "pinapple", "orange"]

# # If we want to add comma as a separator correctly:
# for i in range(0, fruits.__len__()):
#     if i == 0:
#         print(fruits[0], end="")
#     else:
#         print(",", fruits[i], end="")

# for fruit in fruits:
#     print(fruit)

# list = ["element1", 1, True]
# for element in list:
#     print(element)

# list = [[1,2,3,4],["element1", "element2", "element3", "element4"]]
# for element in list:
#     print(element)

# For double list then you can extraxt sublists and get elements with:
# list[0] = [1,2,3,4]
# print(list[0][0])

# subList = list[0]
# print(subList[0])

# secondList = list[1]
# print(secondList[0])

## You can add elements to an empty list:
# list = []
# list.append("Element1") # append means add the element to the end
# list.append("Element2")
# print(list)

# list.pop(0) # this will remove the specified elements (by index)
# print(list)

# list.clear # deletes all the elements
# print(list)

#  list = [1,2,3,4,"Element", 5,6,"Element",7,8,"Element"]
# list.remove("Element") # Remove the specific element ## Only removes the first one (if were are double elements)
# print(list)

## If we would want to delete all the duplicate elements:
# print(list.count("Element"))
# count = list.count("Element")

# for i in range(0,count):
#     list.remove("Element")

# You can also do this using while loop:
# while count > 0:
#     list.remove("Element")
#     count -= 1 # count = count - 1

# print(list)

# countFound = 0
# for i in range(0, list.__len__()):
#     if list[i] == "Element":
#         countFound += 1
#     if countFound == 3:
#         list.pop(i)
#         break

# print(list)

# listA = [1,2,3,4]
# listB = listA
# listA.append(5)
# print(listB)

# We can also use concatination
# list = [1,2,3,4]
# list += [5,6]
# print(list)

# listA = [1,2,3,4]
# listB = listA[:] # : is a slice so it creates the copy of an object
# listB.append(5)

# print(listA)
# print(listB) # Because new element is added on to the copy of the original list, the result is different

# listB = listA[1:3]  # We create a sublist of listA (from second position to the fourth position)
# print(listB)

# If we want to pick elements from the second element to the last one (we don't know how many there are):
# listB = listA[1:]
# print(listB)


# Lets create a loop where we can add many elements to the list:
# list = []

# print("Enter the values below")
# while True:
#     element = input("Enter the number:")
#     if element == "":
#         break
#     number = float(element)
#     list.append(number)

# print(list)

# Let's add the calculation of the sum of all the elements in the list:
# sum = 0

# for number in list:
#     sum += number

# Let's add the average of entered numbers
# average = sum / list.__len__()  # Or we can use len(list)
# print("Sum of all the elements is", sum)
# print("Average of all the elements is", average)

# print(list)
# You can create a new list based on previously made list
# list2 = [element + 1 for element in list]
# print(list2)
# list3 = [element ** 2 for element in list]  # Squared elements
# print(list3)

# list = [1,8,29,19]
# list2 = list * 6  # This means that all the elements are repeated 6 times
# print(list2)
