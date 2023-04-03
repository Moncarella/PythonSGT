import json
class Person:
    def __init__(self, name, lastname,age):
        self.name = name
        self.lastname = lastname
        self.age = age
    def __str__(self) -> str:
        return "Name : " + self.name + ", Last Name : " + self.lastname + ", Age : " + str(self.age)

# persons = [{
#     "name":"Arturs",
#     "last_name":"Olekss",
#     "age":"25"
# },
# {
#     "name":"Jack",
#     "last_name":"Sparrow",
#     "age":"35"
# }]

# with open("Persons.json", "w") as f:
#     json.dump({"persons":persons},f)  #JSONs usually start with an object


# with open("Persons.json", "r") as f:
#     persons=json.load(f) # If we use the load function, it returns a dictionary. The load function does the parsing itself
#     # print(persons)
#     # persons = f.read() # If we use a standard read function, it returns a string
#     # print(type(persons))  # You would then need to parse the string in order to get the different variables
#     f.close()

# persons_objects = list()
# for person in persons["persons"]:
#     persons_obj = Person(person["name"], person["last_name"], person["age"])
#     print(persons_obj)
#     persons_objects.append(persons_obj)

