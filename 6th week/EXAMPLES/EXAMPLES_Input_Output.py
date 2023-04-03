# print("Enter the text below:")

# text = ""
# line = input()
# while line != "EOF":
#     if text == "":
#         text = line
#     else:
#         text += "\n" + line
#     line = input()

# with open("output.txt", "w") as f:
#     # print(text,file=f)
#     f.write(text)

# textlines = []
# line = input()
# while line != "EOF":
#     if len(textlines) == 0:
#         textlines.append(line)
#     else:
#        textlines.append("\n" + line)
#     line = input()

# with open("output.txt", "w") as f:
#     # print(text,file=f)
#     f.writelines(textlines)

delim = ";"
def generate_csv(persons:list,header_line=True):
    filelines = list()

    if header_line == True:
        filelines.append("First Name" + delim + "Last Name" + delim + "Age")#header line

    for person in persons:
        line = person["name"] + delim + person["lastname"] + delim + person["age"]
        filelines.append("\n" + line)
    return filelines

# persons = list()

def add_new_persons(persons:list):
    new_persons = list()
    while True:
        name = input("Enter your Name:\n")
        lastname = input("Enter Last Name:\n")
        age = input("Enter your age:\n")
        person = {"name":name,"lastname":lastname,"age":age}
        new_persons.append(person)
        if input("Do you want to stop? (y)") == "y":
            break
    new_persons_csv = generate_csv(new_persons,header_line=False)
    for person in new_persons_csv:
        persons.append(person)
# with open("Persons.csv","w") as f:
#     f.writelines(generate_csv(persons))


filename = input("Enter the file name:\n")
with open(filename,"r") as f:
    print(f.read())
    f.close()

with open(filename,"r") as f:
    persons = f.readlines()
    f.close()

def delete_entries(persons:list):
    line_numbers = input("Which lines you want to be deleted?").split(" ")
    persons_copy = list()
    for i in range(0,len(persons)):
        if not str(i) in line_numbers:
            persons_copy.append(persons[i])
    return persons_copy

with open(filename,"w") as f:
    action = input("Do you want to delete(d),insert(i)")
    if action == "i":
        add_new_persons(persons)
    elif action == "d":
        persons = delete_entries(persons)
    f.writelines(persons)