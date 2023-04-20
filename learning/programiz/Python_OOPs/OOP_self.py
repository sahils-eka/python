class Student:
    def check_pass_fail(self):
        # the first argument in every python class method should be self.
        # self(or any other name) represnts the OBJECT CALLING it !
        if self.marks >= 40:
            print(f"{self.name} ->Pass")
        else:
            print(f"{self.name} ->Fail")
    a = 10
    li = ['Hello', 2]


s1 = Student()
# Here, 'self' in class method will be pointing or representing the s1 object
s1.name = "Sahil"
s1.marks = 89
s1.check_pass_fail()

s2 = Student()
# Here, 'self' in class method will be pointing or representing the s2 object
s2.name = "Singh"
s2.marks = 36
s2.check_pass_fail()

# Bonus
# dir
"""
To list all the methods and object of a class use dir funtion
"""

d1 = Student()
print(dir(d1))
