from linked_list import LinkedList
from utils import create_list

def add_lists(list1, list2):

    node1 = list1.head
    node2 = list2.head
    carryin = 0
    new_list = None

    while node1 or node2: # ie. not null
        if not node1:
            to_add = node2.get_value() + carryin
        elif not node2:
            to_add = node1.get_value() + carryin
        else:
            to_add = node1.get_value() + node2.get_value() + carryin

        carryin = int((to_add - (to_add % 10)) / 10)
        to_add = to_add % 10

        if not new_list:
            new_list = LinkedList(to_add)
        else:
            new_list.insert_at_end(to_add)

        if node1:
            node1 = node1.next
        if node2:
            node2 = node2.next

    return new_list


def main():
    list1 = create_list(837857)
    list2 = create_list(9888)

    total = add_lists(list1, list2)
    total.print_list()

if __name__ == '__main__':
    main()
