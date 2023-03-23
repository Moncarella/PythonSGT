import re  # You can import a module
# This module checks if the pattern matches or not 
text = "The quick brown fox jumps over the lazy dog."
match = re.search('fox', text)
if match:
    print("Found a match:", match.group())

# text@domain.country
emailPattern = "^[a-zA-Z0-9][a-zA-Z0-9.]*[a-zA-Z0-9]@([a-z0-9]+\.)[a-z]{2,}$" #[a-zA-Z0-9] this looks for pattern in any location inside the string
email = input("Enter the text\n")
match = re.search(emailPattern, email) # Checks pattern inside the text
# Returns the match object
if match:
    print("pattern is correct")
else:
    print("pattern is not correct")

# "^[a-zA-Z0-9]+$" plus means you can search as many characters as you want
# ^[a-zA-Z0-9.]+@[a-z0-9]+\.[a-z]+$     # \. means exactly dot   GENERAL PATTERN FOR EMAILS
# ^[a-zA-Z0-9.]+@[a-z0-9]+\.[a-z]{2,}$   we add the condition that there has to be two or more characters after dot
# ^[a-zA-Z0-9.]+@([a-z0-9]+\.)[a-z]{2,}$   Adding the grouping. The pattern in parenthesis should be repeated atleast once
# ^[a-zA-Z0-9][a-zA-Z0-9.]*[a-zA-Z0-9]@([a-z0-9]+\.)[a-z]{2,}$   Adding a condition where dot cannot appear in the pattern


# Validating phone numbers:
phoneInput = input("Enter the phone:\n")
phonePattern = r'^((\+371|8)( ){0,1}){0,1}2[0-9]{7}$' # we put verbatim r in order to avoid escape characters and some python issues
# the grouping says that the country code is optional
# for lithuanian phone numbers you can use (\+370|8) adding or operator
# ( ){0,1} saying that the space is optional
match = re.search(phonePattern, phoneInput)
if match:
    print("Pattern is correct")
else:
    print("Pattern is not correct")