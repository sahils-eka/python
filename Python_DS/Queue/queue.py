from collections import deque


class Queue():

    def __init__(self):
        self.queue = deque()

    def dequeue(self):
        if len(self.queue) > 0:
            self.queue.popleft()
        else:
            print("Queue is empty")

    def enqueue(self, value):
        self.queue.append(value)

    def get_size(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)


newQueue = Queue()

print(type(newQueue))

print(newQueue.get_size())

newQueue.dequeue()

newQueue.enqueue(22)
newQueue.enqueue(5)
newQueue.enqueue(1998)

newQueue.get_size()

print(newQueue)

newQueue.dequeue()

print(newQueue)
