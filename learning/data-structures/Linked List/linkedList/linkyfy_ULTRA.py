class Node:
    def __init__(self, d=None, n=None):
        self.data = d
        self.next = n

    def __str__(self):
        return ('('+str(self.data)+')')


class LinkedList:
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, data, after=None):
        if after == None:
            newNode = Node(data, self.root)
            self.root = newNode
            self.size += 1
        else:
            curr = self.root
            while curr is not None:
                if curr.data == after:
                    newNode = Node(data, curr.next)
                    curr.next = newNode
                    self.size += 1

                curr = curr.next

    def find(self, value):
        curr = self.root
        while curr is not None:
            if curr.data == value:
                print(value)
                return value
            else:
                curr = curr.next
        print('Not found')
        return None

    def remove(self, value):
        prev = Node()
        curr = self.root
        while curr is not None:
            if curr.data == value:
                if prev is not None:
                    prev.next = curr.next
                else:
                    self.root = curr.next
                self.size - 1
                return True
            else:
                prev = curr
                curr = curr.next
        print('Data to be deleted, not found !')
        return False

    def print(self):
        curr = self.root
        while curr is not None:
            print(curr, end='-->')
            curr = curr.next
        print('End')


linky = LinkedList()

linky.add(2)
linky.add(98)
linky.add(27)
linky.print()
linky.add(66, 98)
linky.add(44, 2)
linky.print()
linky.remove(33)
linky.print()
