def even_gen(max):
    n = 2
    while n <= max:
        yield n
        n += 2


evenNumsObject = even_gen(4)
print(next(evenNumsObject))
print(next(evenNumsObject))
print(next(evenNumsObject))
