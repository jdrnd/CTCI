from stack import Node

# LIFO queue, insertions at head, removals at tail
class Queue(object):

    def __init__(self, value=None):
        if value == None:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            self.head = Node(value)
            self.tail = self.head
            self.length = 1

    # Add to end
    def add(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # Remove from start
    def pop(self):
        value = self.head.value
        self.head = self.head.next
        self.length -= 1
        return value


    def peek(self):
        return self.head.value

    def is_empty(self):
        return self.length == 0
