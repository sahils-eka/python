import builtins


class MinHeap:
    def __init__(self, items=[]):
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self.floatUp(len(self.heap)-1)

    def push(self, value):
        self.heap.append(value)
        self.floatUp(len(self.heap)-1)

    def pop(self):
        if len(self.heap) < 2:
            min = None
        elif len(self.heap) == 2:
            min = self.heap.pop()
        else:
            self.swap(1, len(self.heap)-1)
            min = self.heap.pop()
            self.bubbleDown(1)
        return min

    def bubbleDown(self, index):
        minimum = index
        left = index*2
        right = index*2 + 1
        if len(self.heap) > left and self.heap[left] < self.heap[minimum]:
            minimum = left
        if len(self.heap) > right and self.heap[right] < self.heap[minimum]:
            minimum = right
        if minimum != index:
            self.swap(index, minimum)
            self.bubbleDown(minimum)

    def floatUp(self, index):
        if index <= 1:
            return
        parent = index//2
        if self.heap[index] < self.heap[parent]:
            self.swap(index, parent)
            self.floatUp(parent)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __str__(self):
        return str(self.heap)


li = [23, 13, 17, 11, 12]
heap = MinHeap(li)

print(heap)

# heap.push(9)

# print(heap)

# minimum = heap.pop()
# print(minimum)
# print(heap)
# minimum = heap.pop()
# print(minimum)
# minimum = heap.pop()
# print(minimum)
# minimum = heap.pop()
# print(minimum)
# minimum = heap.pop()
# print(minimum)
# minimum = heap.pop()
# print(minimum)
# minimum = heap.pop()
# print(minimum)
# print(heap)
