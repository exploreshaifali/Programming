class Queue:
    def __init__(self, size):
        self.size = size
        # inserting from tail and removing from front.
        self.front = -1
        self.tail = -1
        self.q = [0 for i in range(size)]

    def is_empty(self):
        if self.front == self.tail == -1:
            return True
        return False

    def is_full(self):
        if (self.tail+1)%self.size == self.front:
            return True
        return False

    def enqueue(self, data):
        if self.is_full():
            return
        if self.is_empty():
            self.tail = 0
            self.front = 0
        else:
            # circular array looping
            self.tail = (self.tail + 1)%self.size
        self.q[self.tail] = data

