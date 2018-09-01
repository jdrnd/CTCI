
class Node(object):
    def __init__(self, value):
        self._value = value
        self.prev = None
        self.next = None

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

class LinkedList(object):
    def __init__(self):
        self.head = Node(None)
        self.tail = self.head
        self._size = 1

    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self._size = 1

    def get_length(self):
        return self._size

    def insert_at_end(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self._size += 1

    def insert_at_start(self, value):
        new_node = Node(value)
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def remove_duplicates(self):
        # Add all node values to dictionary, remove node if value already exists
        values = {}
        node = self.head
        while node != None:
            if values.get(node.get_value()) == None:
                values[node.get_value()] = True
                node = node.next
            else:
                # Node already in list
                next_node = node.next
                self._delete_node(node)
                node = next_node

    def remove_duplicates_nostorage(self):
        node = self.head
        while node != None:
            value = node.get_value()

            node_pt = node.next
            while node_pt != None:
                if node_pt.get_value() == value:
                    temp = node_pt.next
                    self._delete_node(node)
                    node_pt = temp
                else:
                    node_pt = node_pt.next
            node = node.next

    def get_n_from_last(self, n):
        # Treat the list as singly linked here
        # Build a circular buffer of last n elements

        if n == 0:
            return self.tail.get_value()
        else:
            buff = [0] * (n + 1)

            node = self.head
            counter = 0
            while node != None:
                buff[counter % (n + 1)] = node.get_value()
                counter += 1
                node = node.next

            last = counter - 1
            if n > last:
                return "ERROR"
            nth_from_last = last - n
            value = buff[nth_from_last % n]
            return value


    def delete_middle_node(self, node):
        if node == self.head or node == self.tail:
            return "ERROR"

        node.set_value(node.next.get_value())
        self._delete_node(node.next)

    def print_list(self):
        curr_node = self.head
        print('Start -> ', end='')
        while curr_node != None:
            print(str(curr_node.get_value()) + ' -> ',end='')
            curr_node = curr_node.next
        print('End')

    # Move all values equal to or greater than value to after value, all values less than to before
    def partition_about_value(self, value):
        node = self.head

        parition_node_reached = False
        while node != None:
            curr_value = node.get_value()
            _next = node.next

            if value == curr_value:
                parition_node_reached = True
            elif not parition_node_reached:
                if curr_value >= value:
                    self._delete_node(node)
                    self.insert_at_end(curr_value)
            elif parition_node_reached:
                if curr_value < value:
                    self._delete_node(node)
                    self.insert_at_start(curr_value)
            node = _next

    # "Private" Methods

    def _get_node_by_index(self, nodeindex):
        if nodeindex > self._size - 1:
            return "Error"

        node = self.head
        for i in range(0, nodeindex):
            node = node.next
        return node

    def _swap_values_at(self, node1, node2):
        temp = node1.get_value()
        node1.set_value(node2.get_value())
        node2.set_value(temp)

    def _delete_node(self, node):
        if node == self.head:
            self.head = node.next
            self.head.prev = None
        elif node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        node = None # Node's memory will be automatically GC'd
        self._size -= 1

    def _get_first_node_by_value(self, value):
        node = self.head
        while node != None:
            if node.get_value() == value:
                return node
            node = node.next
        return None
