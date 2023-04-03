from EXAMPLES_OOP_Person import Person

class Employee(Person):  # We specify here that employee inherits from class Person (Employee extends Person)

    def __init__(self, name: str, last_name: str, date_of_birth: str, 
                 # age: int, 
                 position:str) -> None:
        self.position = position
        super().__init__(name, last_name, date_of_birth, 
                         # age
                         )

    # We need to add new parameter to the printed string:
    def __str__(self) -> str:   # Overwritting the function from the supper-class/parent class
        return super().__str__() + "\nPosition : " + self.position

