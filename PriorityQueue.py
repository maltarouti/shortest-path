
class PriorityQueue:
    # a constructor that takes a boolean value (true for descending).
    def __init__(self):
        self.elements = list()

    # a function that returns (true: if empty false otherwise).
    def is_empty(self):
        return len(self.elements) == 0

    # a function that inserts a node in the queue based on it's priority.
    def enqueue(self, node):
        self.elements.append(node)
        self.elements.sort(key=lambda x: x.cost)

    # returning the first element and remove it from the queue.
    def dequeue(self):
        if self.is_empty():
            return None
        return self.elements.pop(0)




