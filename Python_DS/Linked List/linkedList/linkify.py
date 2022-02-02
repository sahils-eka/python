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

    def add(self, value):
        new_node = Node(value, self.root)
        self.root = new_node
        self.size += 1

    def find(self, data):
        curr = self.root
        while curr is not None:
            if curr.data == data:
                return data
            else:
                curr = curr.next
        return None

    def remove(self, value):
        prev = Node()
        curr = self.root
        if curr.data == value:  # if data is present in the first node
            self.root = curr.next
            curr = None
            self.size-1
            return True

        # Else iterate through complete list
        while curr is not None:
            if curr.data == value:
                prev.next = curr.next
                self.size-1
                return True
            else:
                prev = curr
                curr = curr.next
        return False

    def print(self):
        curr = self.root
        while curr is not None:
            print(curr, end='-->')
            curr = curr.next
        print('End')


linky = LinkedList()

linky.add(12)

linky.print()

linky.add(29)

linky.print()

linky.add(23)

linky.print()

# print(linky.find(214))

linky.remove(23)
linky.print()
