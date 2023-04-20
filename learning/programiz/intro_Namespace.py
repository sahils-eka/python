'''
What is Name in Python?
Name (also called identifier) is simply a name given to objects. Everything in Python is an object. Name is a way to access the underlying object.

For example, when we do the assignment a = 2, 2 is an object stored in memory and a is the name we associate it with. We can get the address (in RAM) of some object through the built-in function id(). Let's look at how to use it.
'''
a = 6
print(
    f"\nid() will print the address of 'a' in the ram. \na= {a}\nid(a)= {id(a)}\n# Note: You may get different values for the id\n")


'''
What is a Namespace in Python?
Now that we understand what names are, we can move on to the concept of namespaces.

To simply put it, a namespace is a collection of names.

In Python, you can imagine a namespace as a mapping of every name you have defined to corresponding objects.

Different namespaces can co-exist at a given time but are completely isolated.

A namespace containing all the built-in names is created when we start the Python interpreter and exists as long as the interpreter runs.

This is the reason that built-in functions like id(), print() etc. are always available to us from any part of the program. Each module creates its own global namespace.

These different namespaces are isolated. Hence, the same name that may exist in different modules does not collide.

Modules can have various functions and classes. A local namespace is created when a function is called, which has all the names defined in it.
'''
# ------------------------------------------
# Example of Scope and Namespace in Python
# ------------------------------------------
a = 10
# a is in global namespace


def outer_fucntion():
    b = 20
    # b is in local namespace of outer_function

    def inner_function():
        c = 6
        # c is in local namespace of inner_function
        # print("a=", a) # a = 10
        print("b=", b)
        global a
        a = 22
        print("Global a=", a)
    inner_function()


outer_fucntion()
