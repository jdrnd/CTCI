from linked_list import LinkedList
from utils import create_list

def get_intersection_node(list1, list2):
    node1 = list1.head
    node2 = list2.head

    diff = list1.get_length() - list2.get_length()
    print(diff)
    if diff > 0:
        while diff > 0:
            node1 = node1.next
            diff -= 1
    elif diff < 0:
        diff = abs(diff)
        while diff > 0:
            node2 = node2.next
            diff -= 1

    while node1 != node2:
        print(node1, node2)
        print(node1.get_value(), node2.get_value())
        node1 = node1.next
        node2 = node2.next
    return node1

def main():
    list1 = LinkedList(1)
    list1.insert_at_end(2)
    list1.insert_at_end(3)
    list1.insert_at_end(4)
    list1.insert_at_end(5)
    list1.insert_at_end(6)
    list1.insert_at_end(7)
    list1.insert_at_end(8)
    list1.insert_at_end(9)

    list2 = LinkedList(0)
    list2.insert_at_end(0)
    list2.insert_at_end(0)
    list2.insert_at_end(0)
    list2.insert_at_end(0)
    list2._size = 11

    list2.head.next.next.next.next.next = list1.head.next.next.next
    list2.tail = list1.tail

    list1.print_list()
    list2.print_list()

    print(get_intersection_node(list1, list2).get_value())


if __name__ == '__main__':
    main()
