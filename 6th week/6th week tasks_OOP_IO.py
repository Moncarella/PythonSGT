from dataclasses import dataclass

# Task 1
# Create a class named Car that has the following attributes: make, model, and year. It should also have a 
# method called get_info() that returns a string with the car's make, model, and year

class Car:
    def __init__(self, make:str, model:str, year:str) -> None:
        self.make = make
        self.model = model
        self.year = year
    
    def get_info(self):
        return("The car's make : " + self.make + "\nModel : " + self.model + "\nYear of production : " + str(self.year))

car_obj = Car("BMW", "320cd", "2003")
print(car_obj.get_info()) 


# Task 2
# Create a class named Rectangle that has the following attributes: width and height. 
# It should also have methods called area() and perimeter() that return the area and perimeter of the rectangle, respectively

@dataclass
class Rectangle:
    def __init__(self, width:int, height:int) -> None:
        self.width = float(width)
        self.height = float(height)

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
rectangle = Rectangle(2,3)
print("The area of the rectangle is: ", rectangle.area(), "\nThe perimeter of the rectangle is: ", rectangle.perimeter())


# Task 3
# Create a class named BankAccount that has the following attributes: account_number, balance, and owner_name. 
# It should also have methods called deposit() and withdraw() that update the balance accordingly

@dataclass
class BankAccount:
    account_number:str
    balance:float
    owner_name:str

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if amount > self.balance:
            print("Not enough money in your bank account")
        else:
            self.balance -= amount

bank_acc = BankAccount("LT4835820385", 200.23, "Monika")
print(bank_acc)
bank_acc.deposit(100.34)
print(bank_acc)
bank_acc.withdraw(500)
print(bank_acc)


# Task 4
# Create a class named Person that has the following attributes: name, age, and address. 
# It should also have a method called get_info() that returns a string with the person's name, age, and address

@dataclass
class Person:
    name:str
    age:int
    address:str

    def get_info(self):
        return("The person's name is : " + self.name + "\nAge : " + str(self.age) + "\nHome address : " + self.address)
    
person1 = Person("Monika", 27, "Zolynu g.")
print(person1.get_info())


# Task 5
# Create a class named Animal that has the following attributes: name and species. 
# It should also have a method called speak() that returns a string with the animal's sound

@dataclass
class Animal:
    name:str
    species:str

    def speak(self):
        return "Meow"


# Task 6
# Create a base class named Vehicle that has the following attributes: make, model, and year. 
# It should also have a method called get_info() that returns a string with the vehicle's make, model, and year. 
# Then create two subclasses, Car and Truck, that inherit from Vehicle and add additional attributes and methods specific to each type of vehicle

class Vehicle:
    def __init__(self, make:str, model:str, year:str) -> None:
        self.make = make
        self.model = model
        self.year = year
    
    def get_info(self):
        return("The car's make : " + self.make + "\nModel : " + self.model + "\nYear of production : " + str(self.year))
    
class Car(Vehicle):
    def __init__(self, make: str, model: str, year: str, bodytype:str) -> None:
        super().__init__(make, model, year)

        self.bodytype = bodytype

    def get_info(self):
        return super().get_info() + "\nCar's body type : " + self.bodytype
    
    def get_vehicle_body_type(self):
        return("The vehicle's body type is : " + self.bodytype)
    
car_obj = Car("BMW", "320cd", "2003", "coupe")
print(car_obj.get_info()) 
print(car_obj.get_vehicle_body_type()) 

class Truck(Vehicle):
    def __init__(self, make: str, model: str, year: str, weightclass:str) -> None:
        super().__init__(make, model, year)

        self.weightclass = weightclass
    
    def get_info(self):
        return super().get_info() + "\nWeight class : " + self.weightclass
    
    def get_vehicle_weight_class(self):
        return("The truck's weight class is : " + self.weightclass)
    
truck_obj = Truck("BMW", "320cd", "2003", "medium")
print(truck_obj.get_info()) 
print(truck_obj.get_vehicle_weight_class()) 


# Task 7 
# Create a base class named Person that has the following attributes: name, age, and address. 
# It should also have a method called get_info() that returns a string with the person's name, age, and address. 
# Then create two subclasses, Student and Teacher, that inherit from Person and add additional attributes and methods specific to each role

@dataclass
class Person:
    name:str
    age:int
    address:str

    def get_info(self):
        return("The person's name is : " + self.name + "\nAge : " + str(self.age) + "\nHome address : " + self.address)
 
@dataclass
class Student(Person):
    major:str

    def student_major(self):
        return("Student is majoring in : " + self.major)
    
student = Student("Monika", 27, "Kaunas", "Data Science")
print(student)
print(student.student_major())

@dataclass 
class Teacher(Person):
    years_in_teaching:int

    def started_teaching_at(self):
        return("The teacher " + self.name + " started teaching at " + str((self.age - self.years_in_teaching)) + " years old")
    
teacher = Teacher("Martynas", 28, "Kaunas", 4)
print(teacher)
print(teacher.started_teaching_at())


# Task 8
# Write a Python program that reads a JSON file containing a list of dictionaries, sorts the list by a specific key, and writes the sorted list back to the file

import json

key = "name"
with open("Persons.json", "r") as f:
    persons = json.load(f)["persons"]

persons.sort(key=lambda person:person[key])
    
with open("Persons.json", "w") as f:
    json.dump({"persons":persons},f)


# Task 9
# Write a Python program that reads a CSV file containing student grades, calculates their average score, and writes the average to a new file
with open("Student_grades.csv", "r") as f:
    students_grades = f.readlines()[1:]  # Because we don't need to read the header line

averages = list()
for student_line in students_grades[1:]:
    columns = student_line.replace("\n","").split(";")
    name = columns[0]
    sum_grade = 0
    for grade in columns[1:]:
        sum_grade += int(grade)
    averages.append([name, sum_grade/(len(columns)-1)])

csv_output = students_grades[0].replace("\n", "")
for student in averages:
    csv_output += "\n" + student[0] + ";" + str(student[1])

with open("Student_average.csv", "w") as f:
    f.write(csv_output)

# Task 10
# Write a Python program that reads a CSV file containing student grades and writes a new CSV file with the grades sorted by student name
# import csv

lines = list()
with open("Student_grades.csv", "r") as csvfile:
    student_grades_csv = csv.reader(csvfile, delimiter=";")
    for student in student_grades_csv:
        lines.append(student)

student_grades = lines[1:]
student_grades.sort(key= lambda student:student[0])

print(student_grades)
with open("Student_grades.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    writer.writerow(lines[0])
    writer.writerows(student_grades)