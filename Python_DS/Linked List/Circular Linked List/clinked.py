class Node:
    def __init__(self, d=None, n=None):
        self.data = d
        self.next = n

    def __str__(self):
        return ('('+str(self.data)+')')


class CLinkedList:
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, value):
        if self.size == 0:
            self.root = Node(value)
            self.root.next = self.root
        else:
            newnode = Node(value, self.root.next)
            self.root.next = newnode
        self.size += 1

    def remove(self, d):
        curr = self.root
        prev = None
        while True:
            if curr.data == d:
                if prev is not None:
                    prev.next = curr.next
                else:
                    while curr.next != self.root:
                        curr = curr.next
                    curr.next = self.root.next
                    self.root = self.root.next
                self.size -= 1
                return True
            elif curr.next == self.root:
                print('Data not found')
                return False
            else:
                prev = curr
                curr = curr.next

    def print(self):
        curr = self.root
        print(curr, end='-->')
        while curr.next != self.root:
            curr = curr.next
            print(curr, end='-->')
        print(self.root)


clink = CLinkedList()

clink.add(5)
clink.add(7)
clink.add(9)
clink.add(99)
clink.add(11)
clink.print()

clink.remove(99)

clink.print()
