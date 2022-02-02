class MinHeap:
    def __init__(self, item=[]):
        self.heap = [0]
        for i in item:
            self.heap.append(i)
            self.__floatup(len(self.heap) - 1)

    def push(self, value):
        self.heap.append(value)
        self.__floatup(len(self.heap)-1)

    def pop(self):
        if len(self.heap) < 2:
            return "Nothing here"
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            self.__swap(1, len(self.heap)-1)
            max = self.heap.pop()
            self.__bubbleDown(1)

        return max

    def __bubbleDown(self, i):
        min = i
        left = i*2
        right = i*2 + 1
        if len(self.heap) > left and self.heap[left] < self.heap[min]:
            min = left
        if len(self.heap) > right and self.heap[right] < self.heap[min]:
            min = right
        if min != i:
            self.__swap(i, min)
            self.__bubbleDown(min)

    def __floatup(self, i):
        if i <= 1:
            return
        parent = i // 2
        if self.heap[i] < self.heap[parent]:
            self.__swap(i, parent)
            self.__floatup(parent)

    def __str__(self):
        return str(self.heap)

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


li = [12, 5, 9, 3, 10, 6]
heap = MinHeap(li)
print(heap)

heap.push(4)

print(heap)

print(heap.pop())

print(heap)
