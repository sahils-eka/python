# tuples are similar to list BUT tuples are immutable

tu = (1, 5, 9, 3, 6, 2, 5, 1, 7, 5)
# tu2 = [1, 5, 9, 3, 6]
print(type(tu))
# print(type(tu2))

print(tu)
print(f"Count of 5 in tu is: {tu.count(5)}")

print(f"\ntuple.index()\nIndex of value 7 in {tu} is:\n{tu.index(7)}")
