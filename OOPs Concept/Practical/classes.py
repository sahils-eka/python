class Dog:
    # class variable
    attr1 = "mammal"

    # Instance attribute
    # Created when an Object is instantiated
    def __init__(self, name) -> None:
        self.name = name

    def speak(self):
        print(f"My name is {self.name}")


dog1 = Dog("Pluto")
dog2 = Dog("Jumbo")

dog1.speak()

# Object has access to class variable?? -- Yes
print(dog2.attr1)
