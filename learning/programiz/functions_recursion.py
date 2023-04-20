def fact(num):
    if num == 1:
        return 1
    return num * fact(num-1)


fa = fact(5)
print(fa)
