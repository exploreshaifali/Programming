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

    def insertAtHead(self, data):
        new_node = Node(data, pre=None, nex=self.head)
        self.head.pre = new_node
        self.head = new_node

    def insertAtTail(self, data):
        temp = self.head
        while temp.nex is not None:
            temp = temp.nex
        new_node = Node(data, pre=temp, nex=None)
        temp.nex = new_node

    def travel(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.nex
