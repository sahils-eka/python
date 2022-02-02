s1 = {1, 2, 5, 6, 7, 9, 8, 3}
s2 = {9, 8, 3, 2, 5}

print("union", s1 | s2)  # union
print("intersection", s1 & s2)  # intersection

print(s1 <= s2)  # checks if s1 is subset of s2

print(s1 >= s2)  # checks if s2 is subset of s1

print(s1-s2)
print(s2-s1)  # this will print null or just set() as all the elements of s2 are in s1

# the ^ includes elements that are in one or the other set but not in both
print(s1 ^ s2)
print(s2 ^ s1)
