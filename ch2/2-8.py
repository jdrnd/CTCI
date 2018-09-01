from linked_list import LinkedList

def get_first_node_in_loop(list1):
    node1 = list1.head
    node2 = list1.head

    # Move forward once so that nodes are not equal
    try:
        node1 = node1.next
        node2 = node2.next.next
    except:
        return None
    # Get intersection node in loop
    while node1 != node2:
        node1 = node1.next
        node2 = node2.next.next

    # Move node1 to head, now both nodes are same distance from first node in loop
    node1 = list1.head
    while node1 != node2:
        node1 = node1.next
        node2 = node2.next

    return node1

def main():
    list1 = LinkedList(0);
    list1.insert_at_end(0)
    list1.insert_at_end(9)
    list1.insert_at_end(1)
    list1.insert_at_end(2)
    list1.insert_at_end(3)
    list1.tail.next = list1.head.next.next
    list1.tail = None

    #list1.print_list()
    print(get_first_node_in_loop(list1).get_value() )

if __name__ == '__main__':
    main()
