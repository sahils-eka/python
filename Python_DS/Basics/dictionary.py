# d1 = dict()
# print(type(d1))

# we can create a dict in python using a list of tuples
# l = [('fname', 'sahil'), ('lname', 'singh'), ('age', 23)]

# d2 = dict(l)

# print(d2)

# we can create a dict in python using a list of lists
# l = [['name', 'sahil'], ['lname', 'singh'], ['age', 23]]
# d = dict(l)
# print(d)
# print(d['age'])

# # Another imp way to create a dict is
d = dict(fname='sahil', lname='singh', age=23)
# # print(d)
# # print(d['lname'])

# # Dict operation

d['E-game'] = "Fifa"
d['m-game'] = 'COD'
print(d)

# del(d['m-game'])

# print(d)

print("Mobile game ?", 'COD' in d)
print("E-Game ?", 'E-game' in d)

# print("keys: ", d.keys())  # returns a list of keys
# print("Values: ", d.values())  # returns list of values
# print(d.items())  # gives key:value pair in form of tuples
