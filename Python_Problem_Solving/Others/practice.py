class A():
    def show(self):
        print("This is class A")


class B(A):
    def show(self):
        print("This is class B")
        super().show()


class C():
    def show():
        print("This is class C")


class D(A, C):
    def __init__(self):
        print("I think i am in D")
        super().show()


a = A()
a.show()
b = B()
b.show()

d = D()
d.show()
