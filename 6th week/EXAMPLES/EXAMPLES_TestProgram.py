# from EXAMPLES_OOP_Person import Person
from EXAMPLES_Inheritance import Employee
from EXAMPLES_Polymorphism import Student
from EXAMPLES_OOP_Person import calculate_age  # We import a function from class Person
from EXAMPLES_OOP_Person import Person
from EXAMPLES_Obsolete import Obsolete

# person_obj = Person("Arturs", "Olekss", "01111997", 25)

# print(person_obj)
# Person.print_number_of_functions()
# print("The Persons are " + Person.species)

# person_obj1 = Person("Janis", "Ozolins", "01011998", 25)
# print("Sum of ages : " + str(Person.count_total_age([person_obj, person_obj1])))

employee = Employee("Artus", "Olekss", "01111997", "Programmer")
student = Student("Jack", "Peterson", "16032003", "Master")
print(calculate_age(employee))
print(calculate_age(student))

person_obj1 = Person("Janis", "Ozolins", "01011998")
print(isinstance(person_obj1,Obsolete))

# print(employee) # Every parameter is inherited from the class Person

# If the defined class is not in the same folder then we should specife a path to the class, for example:
# from FolderName.Date import Date

# class Empty:
#     pass

# obj = Empty()
# obj.param1 = "12121"
# obj.param2 = "212122"

# print(obj.param1)
# print(obj.param2)