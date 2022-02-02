"""
You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, 
alphabetical characters, digits, lowercase and uppercase characters.
"""

s = input("Enter the string: ")

print(any(char.isalnum() for char in s))
print(any(char.isalpha() for char in s))
print(any(char.isdigit()for char in s))
print(any(char.islower()for char in s))
print(any(char.isupper()for char in s))
