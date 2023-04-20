'''
Python Decorators
A decorator takes in a function, adds some functionality and returns it. In this tutorial, you will learn how you can create a decorator and why you should use it.
'''


def func_decorator(func):
    def inner():
        print(f"Executing {func.__name__} function")
        func()
        print("Finished Execution")
    return inner


@func_decorator
def printer():
    print("Hello World")


printer()
