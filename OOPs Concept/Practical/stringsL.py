import re
"""
name = "saaaahil"

# endswith
print(name.endswith("il"))

# count

print(name.count("a"))
"""

# Replace method
'''
letter = """
Hi,

Thank you for your email <NAME>.

We are glad to inform you that you have been selected as a <ROLE>.

Date: <DATE>

Best of luck!

"""
letter = letter.replace("<NAME>", "Sahil Singh")
letter = letter.replace("<DATE>", "22nd Feb 2022")
letter = letter.replace("<ROLE>", "Python Developer")
print(letter)
'''

# Double spaces in a string
statement = "Hey there,  how you doin?  :)  "
space = re.findall('\s\s', statement)
print(f"Found {len(space)} white space(s) in the statement")

# using find
statement.find('  ')
