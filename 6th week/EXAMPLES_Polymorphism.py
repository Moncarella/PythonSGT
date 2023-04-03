from EXAMPLES_OOP_Person import Person

class Student(Person):
    def __init__(self, name: str, last_name: str, date_of_birth: str, 
                 # age: int, 
                 level:str) -> None:
        self.level = level
        super().__init__(name, last_name, date_of_birth, 
                         # age
                         )