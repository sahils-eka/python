class Stack():
    def __init__(self):
        self.stack = list()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()

        else:
            print("Stack is empty")

    def peek(self):
        if len(self.stack) > 0:
            print(self.stack[len(self.stack)-1])
        else:
            print("Stack is empty")

    # this is for printing the whole stack
    def __str__(self):
        return str(self.stack)


newStack = Stack()

print(type(newStack), newStack)

newStack.pop()

newStack.push(10)
newStack.push(22)
print(newStack)

newStack.pop()
print(newStack)

newStack.push(5)

newStack.peek()
