# Task 1
# Ask the user to enter the text and a letter. Count how many occurrences of the letter provided
import re

text = input("Please enter the text:\n")
letter = input("Please enter a letter to find in the text:\n")
match = len(re.findall(letter, text))

if match:
    print("There are", match, "occurencies of", letter, "in the provided text")
else:
    print("Your specified letter is not in the text")


# Task 1.1
# Based on the task 1, count the occurrences of each character in the text provided and display them in the output

text = input("Please enter the text:\n")
letters = []
letterCount = []

for i in range(0, text.__len__()):
    letterExist = False
    if text[i] == " ":
        continue
    for j in range(0, letters.__len__()):
        if letters[j] == text[i]:
            letterCount[j] += 1
            letterExist = True
            break
    if not letterExist:
        letters.append(text[i])
        letterCount.append(1)

for i in range(0, letters.__len__()):
    print(letters[i] + " : " + str(letterCount[i]))


# Task 2
list = [10, 5, 3, -1, -4, 0, 1, 8, -15]
# list = ["a", "c", "s", "r", "b"]

for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if list[i] > list[j]:      # Use list[i] < list[j] to sort in descending order
            list[i], list[j] = list[j], list[i]


print(list)





