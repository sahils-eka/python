class MaxHeap:
    def __init__(self, items=[]):
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self.__floatup(len(self.heap)-1)

    def peek(self):
        return self.heap[1]

    def push(self, value):
        self.heap.append(value)
        self.__floatup(len(self.heap) - 1)

    def __str__(self):
        return str(self.heap)

    def __floatup(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatup(parent)

    def popOut(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap)-1)
            max = self.heap.pop()
            self.__bubbledown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __bubbledown(self, index):
        largest = index
        left = index*2
        right = index*2 + 1
        if len(self.heap) > left and self.heap[left] > self.heap[largest]:
            largest = left
        if len(self.heap) > right and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbledown(largest)


li = [1, 4, 7, 5, 2]
heap = MaxHeap(li)
print(heap)
heap.push(11)
print(heap)
print(heap.peek())
heap.popOut()
print(heap)
