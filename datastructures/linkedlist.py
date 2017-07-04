class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self._next = next


class LinkedList:
    def __init__(self, data=None):
        if data is None:
            self.head = None
        else:
            self.head = Node(data)
