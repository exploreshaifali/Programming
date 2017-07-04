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

    def travel(self):
        """Print all element in linked-list link-wise."""
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp._next
