class Student:
    def check_pass_fail(self):
        # the first argument in every python class method should be self.
        # self(or any other name) represnts the OBJECT CALLING it !
        if self.marks >= 40:
            print(f"{self.name} ->Pass")
        else:
            print(f"{self.name} ->Fail")

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def pr(self):
        print(
            f"The student name is {self.name} and their marks = {self.marks}")


class Details(Student):
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Method overriding
    def pr(self):
        print(f"Name: {self.name} | Marks: {self.marks}")
        print("Below is the result from super().pr() method")
        # Using super function
        super().pr()
        '''
        super() creates a temp object of class Student, which then can be used to access class variables
        and methods.
        Simply put, super() acts here as an object of the class Student
        '''


d1 = Details("Sahil", 94)
d1.pr()
s1 = Student("Sahil", 97)
'''
Two built-in functions isinstance() and issubclass() are used to check inheritances.

The function isinstance() returns True if the object is an instance of the class or other classes derived from it. Each and every class in Python inherits from the base class object.
'''
print(f"'d1' is an object of 'Details'?: {isinstance(d1, Details)}")
print(f"'s1' is an object of 'Details'?: {isinstance(s1, Details)}")
print(f"'Details' is a subclass of 'Student'?: {issubclass(Details, Student)}")
print(f"'Student' is a subclass of 'Details'?: {issubclass(Student, Details)}")

'''
Python Multiple Inheritance
In this tutorial, you'll learn about multiple inheritance in Python and how to use it in your program. You'll also learn about multi-level inheritance and the method resolution order.

Python Multiple Inheritance
A class can be derived from more than one base class in Python, similar to C++. This is called multiple inheritance.

In multiple inheritance, the features of all the base classes are inherited into the derived class. The syntax for multiple inheritance is similar to single inheritance.

Here, the MultiDerived class is derived from Base1 and Base2 classes.

The MultiDerived class inherits from both Base1 and Base2 classes.
Example:
'''


class Base1:
    pass


class Base2:
    pass


class MultiDerived(Base1, Base2):
    pass


'''
Python Multilevel Inheritance
We can also inherit from a derived class. This is called multilevel inheritance. It can be of any depth in Python.

In multilevel inheritance, features of the base class and the derived class are inherited into the new derived class.

An example with corresponding visualization is given below.


Here, the Derived1 class is derived from the Base class, and the Derived2 class is derived from the Derived1 class.
'''


class Base:
    pass


class Derived1(Base):
    pass


class Derived2(Derived1):
    pass


'''
Method Resolution Order in Python
Every class in Python is derived from the object class. It is the most base type in Python.

So technically, all other classes, either built-in or user-defined, are derived classes and all objects are instances of the object class.

# Output: True
print(issubclass(list,object))

# Output: True
print(isinstance(5.5,object))

# Output: True
print(isinstance("Hello",object))

In the multiple inheritance scenario, any specified attribute is searched first in the current class. If not found, the search continues into parent classes in depth-first, left-right fashion without searching the same class twice.
So, in the above example of MultiDerived class the search order is [MultiDerived, Base1, Base2, object]. This order is also called linearization of MultiDerived class and the set of rules used to find this order is called Method Resolution Order (MRO).

MRO must prevent local precedence ordering and also provide monotonicity. It ensures that a class always appears before its parents. In case of multiple parents, the order is the same as tuples of base classes.

MRO of a class can be viewed as the __mro__ attribute or the mro() method. The former returns a tuple while the latter returns a list.

'''
print(MultiDerived.mro())
