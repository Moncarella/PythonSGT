# class Person:
#     # pass - to escape error and pass object with no parameters 
#     name:str
#     last_name:str
#     date_of_birth:str

# ao = Person()
# ao.name = "Arturs"
# ao.last_name = "Olekss"
# ao.date_of_birth = "01011990"

# print(ao.name)
# print(ao.last_name)
# print(ao.date_of_birth)

# pers2 = Person()
# pers2.name = "Monika"
# pers2.last_name = "Ras"
# pers2.date_of_birth = "02011996"

# print(pers2.name)
# print(pers2.last_name)
# print(pers2.date_of_birth)


# class Person:
#     def __init__(self) -> None: # constructor
#         print("Hello")

# person_obj = Person() # The code above will only print Hello after we assign an object to it


from EXAMPLES_OOP_Date import Date
from EXAMPLES_Obsolete import Obsolete
class Person:

    species = "Homo sapiens" # You can specify the parameter at the start and then use it for functions
    def __init__(self, name:str, last_name:str, date_of_birth:str, 
                 # age:int
                 ) -> None:
        self.name = name
        self.last_name = last_name
        self.date_of_birth = Date(date_of_birth)
        # self.age = age
    
    def __str__(self) -> str: # We can overwrite generic functions
        return "Name : " + self.name + "\nLast Name : " + self.last_name + "\nDate of birth : " + str(self.date_of_birth)

    def print_number_of_functions():
        print("There are 2 functions in the class Person")

    # def get_genys_species():
    #     return "Homo sapiens"
    
    def get_genys_species():
        return Person.species
    
    # def count_total_age(person_list:list) -> int:
    #     age = 0
    #     for person in person_list:
    #         age += person.age
    #     return age
    
# def print_person(person:Person):
#     print("Name : " + person.name)
#     print("Last Name : " + person.last_name)
#     print("Date of birth : " + person.date_of_birth)
# print_person(person_obj) # This code works when it is written this way

# person_obj = Person("Arturs", "Olekss", "01111997", 25)
# print(person_obj) # The function __str__ is called
# Person.print_number_of_functions() # This code doesn't require objects. The function is general for everyone, not specific to one object
# print("The Persons are " + Person.get_genys_species())

# You can also access a parameter directly:
# print("The Persons are " + Person.species)

# person_obj1 = Person("Janis", "Ozolins", "01011998", 25)
# print("Sum of ages : " + str(Person.count_total_age([person_obj, person_obj1])))

# If we did this in a new file, we can import a class:
# from Person import Person # From Person file import Person class

def calculate_age(person:Person):
    age = 2023 - person.date_of_birth.year
    return age