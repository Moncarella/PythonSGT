# Task 1
text = input("Enter the text:\n")
letter = input("Enter the letter:\n")
count = 0

for i in range(0, len(text)):
    if text[i] == letter:
        count += 1

print("There are " + str(count) + " occurencies of " + letter + " in the text provided")

# Task 1.1

text = input("Please enter the text:\n")
letters = []
letterCount = []

for i in range(0, len(text)):
    letterExist = False
    if text[i] == " ":
        continue
    for j in range(0, len(letters)):
        if letters[j] == text[i]:
            letterCount[j] += 1
            letterExist = True
            break
    if not letterExist:
        letters.append(text[i])
        letterCount.append(1)

for i in range(0, len(letters)):
    print(letters[i] + " : " + str(letterCount[i]))


# Task 2
# Bubble sort

# elements = [1,5,-10,5,8,3]
elements = ["a", "c", "e","z"]

#n = len(elements)

for i in range(0, len(elements)): #n * n
    for j in range(0, len(elements)-i-1):
        if elements[j] < elements[j+1]:
            elements[j], elements[j+1] = elements[j+1], elements[j]
    print(elements)

print(elements)
