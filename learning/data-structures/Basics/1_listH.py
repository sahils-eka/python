# list comprehension
from tkinter import TRUE


x = 2
y = 2
z = 2
n = 2

li = [[i, j, k] for i in range(x) for j in range(y)
      for k in range(z) if i+j+k != n]

# print(li)

# common operation on list
data = [7, 2, 5, 1, 12, 9, 0, 1]

# insert() is used to add a value at a specific index
data.insert(4, 23)
print(f"Found 1 at index={data.index(1)}")

# This will throw an error
# print(f"Found 22 at index={data.index(22)}")


# remove() will delete a value, first occurence only- Note it works on actuall value
data.remove(23)
print(data)

# pop() - used to remove a value on the basis of index provided and returns it.
rem = data.pop(2)
print(rem)
data.sort(reverse=TRUE)
print(data)

# count
print(f"Count of 1 in data is: {data.count(1)}")

# index
print(f"Index of 12 is {data.index(12)}")

data.reverse()
print(f"Data after reversing the order= {data}")
