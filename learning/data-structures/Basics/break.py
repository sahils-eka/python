# break instructs the python program to exit the loop.
for i in range(10):
    if i == 6:
        print(
            f"we got i= {i}, now the 'break' will exit the loop and nothing will be printed after this")
        break
    else:
        print(i)

# continue instructs the python program to skip and jump/execute next statment
for i in range(8):
    if i % 2 == 0:
        continue
    else:
        print(i)
# this code will print just the even number
