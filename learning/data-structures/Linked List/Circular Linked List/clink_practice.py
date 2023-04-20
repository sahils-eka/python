class Node:
    def __init__(self, d=None, n=None):
        self.data = d
        self.next = n

    def __str__(self):
        return ('('+str(self.data)+')')


class Clinked:
    def __init__(self):
        self.size = 0
        self.root = None

    def add(self, value):
        if self.size == 0:
            self.root = Node(value)
            self.root.next = self.root
        else:
            newnode = Node(value, self.root.next)
            self.root.next = newnode
        self.size += 1
        return True

    def remove(self, value):
        curr = self.root
        prev = Node()
        while True:
            if curr.data == value:
                if prev is not None:
                    prev.next = curr.next
                else:
                    while curr.next != self.root:
                        curr = curr.next
                    curr.next = self.root.next
                    self.root = self.root.next
                self.size -= 1
                return True
            else:
                prev = curr
                curr = curr.next
            print('Data not found !!')
            return False

    def print(self):
        curr = self.root
        print(curr, end='-->')
        while curr.next != self.root:
            curr = curr.next
            print(curr, end='-->')
        print(self.root)


clink = Clinked()
clink.add(5)
clink.add(54)
clink.add(88)
clink.add(23)
clink.add(42)
clink.print()

clink.remove(23)
clink.print()
print(clink.size)
