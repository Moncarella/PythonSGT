# Task 1.1 from the 4th week
# text = input("Enter the text:\n")
# letters = {}  # We initialize the dictionary

# for letter in text:  # The code goes through all the characters of string
#     count = letters.get(letter)   # gets the value, based on the key for the dictionary
#     if count == None:       # If there is no such key-value pair, then None is returned
#         letters[letter] = 1    # add a new element to the dictionary, where key is letter and value is the count of the letter
#     else: 
#         count += 1       # increment count received above
#         letters[letter] = count     # Change the value for the count of the letter

# print(letters)

# Dictionaries allow us to get the keys and their values in the same list
# print(letters.get("e")) # If the key exists, then it returns the value mapped to the key
# print(letters.get("x")) # If the key doesn't exist, then it returns None
# print(letters["e"]) # A different way to write the syntax, but it returns an error if there's no such key

# Data for values in dictionaries can be of any type:
person1 = {"Name" : "Monika", "Last Name" : "Rasim", 
           "Info" : ["Female", "Student"]}
print(person1)

# If you want to remove the value from a dictionary
person1.pop("Name")   # Or del person1["Name"] - the result will be the same
print(person1)

# You can also separate the keys and values with:
print(person1.values())
print(person1.keys())
print(person1.items())
# All of these returns tuples
