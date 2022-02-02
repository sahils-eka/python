import random

under_10 = [x for x in range(10) if x % 2 == 0]
print(under_10)

squares = [x**2 for x in range(10) if x % 2 != 0]
print("Odd num squares: ", squares)

chat = 'I l0ve 2 go to the store 7 times a w3ek'

chatnums = [x for x in chat if x.isnumeric()]

nums = ''.join(chatnums)

print(type(nums), nums)

print("Numbers used in the chat is: ", ''.join(chatnums))
