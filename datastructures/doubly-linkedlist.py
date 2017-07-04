class Node:
    def __init__(self, data=None, pre=None, nex=None):
        self.data = data
        self.pre = pre
        self.nex = nex


class DoublyLinkedList:
    def __init__(self, data=None):
        if not data:
            self.head = None
        else:
            self.head = Node(data)
