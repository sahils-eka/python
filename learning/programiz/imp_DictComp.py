# The minimal syntax for dictionary comprehension is:
#dictionary = {key: value for vars in iterable}
'''
print(
    "###----Dictionary Comprehension----###\nThe minimal syntax for dictionary comprehension is:\ndictionary = {key: value for vars in iterable}\n###-----------------###\n")
'''

# 1
old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}

dollar_to_rs = 74

new_price = {item: value*dollar_to_rs for (item, value) in old_price.items()}

print(f"Price in Dollars: {old_price}\nPrice in rupees: {new_price}")

# 2
print("\n")
original_dict = {'jack': 38, 'michael': 48,
                 'guido': 57, 'john': 33, 'sahil': 23, 'rahul': 21}
even_age = {name: age for (name, age) in original_dict.items() if age % 2 == 0}
print(f"Original dict= {original_dict}")
print(f"Even age dict= {even_age}")

# 3
new_dict = {name: age for (
    name, age) in original_dict.items() if age > 20 if age < 40}
print(f"New age dict= {new_dict}")

# 4
old_dict = {key: ('Old' if val > 35 else 'Young')
            for (key, val) in original_dict.items()}
print(old_dict)

# 5
# making of old_dict
old_copy = old_dict.copy()
print(
    f"\n\nid:value of old_dict = {id(old_dict)} : {old_dict}\nid:value of old_copy = {id(old_copy)} : {old_copy}\n")
