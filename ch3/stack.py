
# An implimentation of a stack based off a singly-linked structure
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack(object):

    def __init__(self, value=None):
        if value != None:
            self.top = Node(value)
            self.length = 1
        else:
            self.top = None
            self.length = 0

    # Remove and return the top value from the stack
    def pop(self):
        value = None
        if self.length > 0:
            value = self.top.value
            self.top = self.top.next
            self.length -= 1
        return value

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1

    def peek(self):
        value = None
        if self.length > 0:
            value = self.top.value
        return value

    def is_empty(self):
        return self.length == 0
