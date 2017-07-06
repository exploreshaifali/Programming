class Node:
    def __init__(self, data=None, nex=None):
        self.data = data
        self.nex = nex


class Queue:
    def __init__(self, data=None):
        if data is None:
            # inserting from tail and removing from head
            self.head = None
            self.tail =None
        else:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node

    def enqueue(self, data):
        new_node = Node(data)
        if (self.tail is None) and (self.head is None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.nex = new_node
            self.tail = new_node
