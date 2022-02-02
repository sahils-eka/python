#Python program to swap two elements in a list

'''
Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.

Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]
'''

#Using the pop and insert operations
'''
def swapElements(li,p1,p2):
    v1 = li.pop(p1-1)
    print(v1)
    v2 = li.pop(p2-2)
    print(v2)
    print(len(li))
    li.insert(p1-1, v2)
    li.insert(p2-1, v1)
    return li

li = [23, 65, 19, 90]
pos1, pos2 = 1, 3
print(f"position 1 is {pos1} ; and position 2 is {pos2}")
print(swapElements(li,pos1,pos2))
'''

#Approach 2: Using tuple variable

def swapElements(li, p1,p2):
    tup = li[p1],li[p2]
    li[p2], li[p1] = tup #this will swap put tup[0] in li[p2] and tup[1] into li[p1]
    return li
    
    
li = [23, 65, 19, 90]
pos1, pos2 = 1, 3
print(f"Original list is: {li}. Positions to swap: {pos1} with {pos2}")
print(swapElements(li,pos1-1,pos2-1))