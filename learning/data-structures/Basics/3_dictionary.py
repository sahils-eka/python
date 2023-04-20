myDict = {
    "name": "Sahil Singh",
    "age": 23,
    "About": ["Dev", {"Exp": 3}, [22, 3, 1998]]
}

# Updating a dict using update()

addValues = {'Loves to Play': 'Fifa'}

myDict.update(addValues)
print(f"{myDict.get('salary')}")  # this will return None
# Important
# print(f"{myDict['salary']}")  # This will throw an error
# print(myDict)
# print(myDict["About"])
# print(type(myDict["About"][1]))
# print(type(myDict["About"][2]))
print(myDict.keys())
dili = myDict.keys()
print(f"this is dili= {dili}")
print(f"Type of dili= {type(dili)}")
print(type(myDict.keys()))
# Important
key = list(myDict.keys())
print(f"Type of key is {type(key)}")
print(key)

#Items in dict
items = myDict.items()
print(f"This is dict.items(): {items}")
print(f"Type of dict.items(): {type(items)}")
items = list(myDict.items())
print(f"Type of items of dict.item(): {type(items[0])}")


# # d1 = dict()
# # print(type(d1))

# # we can create a dict in python using a list of tuples
# # l = [('fname', 'sahil'), ('lname', 'singh'), ('age', 23)]

# # d2 = dict(l)

# # print(d2)

# # we can create a dict in python using a list of lists
# # l = [['name', 'sahil'], ['lname', 'singh'], ['age', 23]]
# # d = dict(l)
# # print(d)
# # print(d['age'])

# # # Another imp way to create a dict is
# d = dict(fname='sahil', lname='singh', age=23)
# # # print(d)
# # # print(d['lname'])

# # # Dict operation

# d['E-game'] = "Fifa"
# d['m-game'] = 'COD'
# print(d)

# # del(d['m-game'])

# # print(d)

# print("Mobile game ?", 'COD' in d)
# print("E-Game ?", 'E-game' in d)

# # print("keys: ", d.keys())  # returns a list of keys
# # print("Values: ", d.values())  # returns list of values
# # print(d.items())  # gives key:value pair in form of tuples
