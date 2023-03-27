my_tuple = "apple", "banana", "orange"
print(my_tuple)

def myFunc():
    return 3,7

print(myFunc())

my_tuple[10] = "Test" # That's not possible because tuples are not mutable
print(my_tuple[0])

my_tuple1 = "Test12", "YTest"

my_tuple = my_tuple1  # You cannot change elements in the tuple but it's possible to asign tuple to another tuple (change the variable)

# You can also create a tuple with:
a,b,c = my_tuple
# Same as
a = my_tuple[0]
b = my_tuple[1]
c = my_tuple[2]

# Tuples can be used as keys for dictionaries
person = {("Name", "Last Name") : ("Arturs", "Olekss"), "Height":179, "Weight":75}
print(person)
# You can access the dictionary like this:
print(person[("Name", "Last Name")])

# Functions of tuples:
print(sorted(my_tuple))
print(max(my_tuple))