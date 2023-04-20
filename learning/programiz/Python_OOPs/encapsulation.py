'''
# Encapsulation
Using OOP in Python, we can restrict access to methods and variables. This prevents data from direct modification which is called encapsulation. In Python, we denote private attributes using underscore as the prefix i.e single _ or double __.
'''


class Compute:
    def __init__(self):
        self.__maxprice = 900
        # Here __maxprice is a private attribute of this class

    def sell(self):
        print(f"Max price of device= {self.__maxprice}")

    def priceSetter(self, price):
        self.__maxprice = price

# Outputs/Explanation


s1 = Compute()
s1.sell()
# Output will be --> Max price of device= 900

s2 = Compute()
# lets try to edit the max price
s2.__maxprice = 1100
s2.sell()
# Here, the output should be 1100 right? But no, it will be 900 only because you cannot update a private
# value direclty outside the class defination.

# Output will be --> Max price of device= 900

# Now let's change the max value using a class setter method.
s3 = Compute()
# Calling a setter method which takes a value and updates the private variable.
s3.priceSetter(1200)
s3.sell()
# Output --> Max price of device= 1200
