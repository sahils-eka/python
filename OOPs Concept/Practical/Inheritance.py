class Person:
    def __init__(self, name, idno):
        self.name = name
        self.idno = idno

    def display(self):
        print(f"Name= {self.name}")
        print(f"ID= {self.idno}")


class Employee(Person):
    def __init__(self, namex, idnumber, salary, post):
        self.salary = salary
        self.post = post
        # You can either use super() or the Parent class name. Upto you!
        super().__init__(namex, idnumber)

    def details(self):
        print(f"My name is {self.name}")
        print(f"ID Number: {self.idno}")
        print(f"Post: {self.post}")
        print(f"Salary={self.salary}")


person1 = Person("Rex", 1662)

person1.display()

Emp1 = Employee("Sass", 1789, 128237, "Engineer")

Emp1.display()
Emp1.details()
