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


s1 = Student("Sahil", 92)
s2 = Student("Lola", 39)

s1.check_pass_fail()
s2.check_pass_fail()
