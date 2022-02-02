# Python program to interchange first and last elements in a list
'''
Given a list, write a Python program to swap first and last element of the list.
Examples: 
Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]
Input : [1, 2, 3]
Output : [3, 2, 1]
'''

# My solution
'''
li = []
n = int(input("Enter the size of the list: "))
for i in range(n):
    value = int(input(f"Enter the element number {i+1}: "))
    li.append(value)

temp = li[0]
li[0] = li[len(li)-1]
li[len(li)-1] = temp

print(li)
'''

# GFG solution
# 1
li = [12, 35, 9, 56, 24]
a, *b, c = li  # deserailizing

li[0] = c
li[len(li)-1] = a
print(li)
