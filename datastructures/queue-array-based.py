class Queue:
    def __init__(self, size):
        self.size = size
        # inserting from tail and removing from front.
        self.front = -1
        self.tail = -1
        self.q = [0 for i in range(size)]
