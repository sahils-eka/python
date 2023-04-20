s = {1, 4, 6}
print(type(s))
print(s)

# Important - This will create empty dict rather than a set
a = {}
print(f"Type of a is: {type(a)}")

# To create empty set
b = set()
print(f"Type of b is: {type(b)}")

# Adding the values
# s.add('sahil')

# print(s)

# printing any value on a given index
# print(s[0])

# Can add tuples in the set as they tuple() are Immutable
s.add((11, 23))
# print(s)

# Can we add dict() in set? No we cannot as dict() are unhashable and mutable
# s.add({"Role": "Python Dev"})
# print(s)

# Can we add set() in a set? No we cannot as set() are unhashable and mutable
# s.add({11, 56, 70})
# print(s)

# Cannot add list in the set as Lists are unhashable and Mutable
# s.add([7, 8, 9])

# UNION
newSet = s.union({7, 13, 15})
print(f"UNION is {newSet}")
# >> {(11, 23), 1, 4, 6, 7, 13, 15}

# INTERSECTION
inter = newSet.intersection({1, 5, 7, 10})
print(f"INTERSECTION of newSet and other set is: {inter}")
# >> INTERSECTION of newSet and other set is: {1, 7}

inter2 = newSet.intersection([1, 4, 7, 23, 11])
print(f"Intersection of set and list: {inter2}")

# Problem_1

s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(s)
# >> {'20', 20} - Why? Because 20 == 20.0 (and set doesn't include duplicate values)
