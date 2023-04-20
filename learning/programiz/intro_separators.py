'''
The sep separator is used between the values. It defaults into a space character.
'''

print(1, 2, 3, 4, 5, 6, 7, sep="<>")

'''
After all values are printed, end is printed. It defaults into a new line.
'''
for i in range(1, 10):
    print(i, end="->")
