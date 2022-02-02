class Node:
    def __init__(self, d=None, n=None):
        self.data = d
        self.next = n

    def __str__(self):
        return str('('+str(self.data)+')')


class LinkedList:
    def __init__(self):
        self.size = 0
        self.root = None

    def add(self, value, after=None):
        if after == None:
            newNode = Node(value, self.root)
            self.root = newNode
            self.size += 1
        else:
            curr = self.root
            while curr is not None:
                if curr.data == after:
                    newNode = Node(value, curr.next)
                    curr.next = newNode
                    self.size += 1
                    return True
                else:
                    curr = curr.next
            print('Data not found !')
            return False

    def remove(self, value):
        curr = self.root
        prev = Node()
        while curr is not None:
            if curr.data == value:
                if prev is not None:
                    print('prev')
                    prev.next = curr.next
                else:
                    print('prev is none')
                    self.root = curr.next
                self.size -= 1
                return True
            else:
                prev = curr
                curr = curr.next
        print('Data not found')
        return False

    def find(self, value):
        curr = self.root
        while curr is not None:
            if curr.data == value:
                return value
            else:
                curr = curr.next
        print('Value not present')
        return False

    def print(self):
        curr = self.root
        while curr is not None:
            print(curr, end='-->')
            curr = curr.next
        print('End')


llist = LinkedList()

llist.add(5)
llist.add(22)
llist.add(98)
print(llist.size)
llist.print()
llist.add(11, 22)
llist.print()
llist.remove(22)
llist.print()
