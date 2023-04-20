class Even:
    def __init__(self, max):
        self.n = 2
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.max:
            result = self.n
            self.n += 2
            return result
        else:
            raise StopIteration


num = Even(10)
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
# this will throw an error, num = 12
print(next(num))
