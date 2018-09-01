from linked_list import LinkedList
from utils import create_list

def main():
    list = create_list()
    list.print_list()
    list.remove_duplicates()
    list.print_list()

    list = create_list()
    list.print_list()
    list.remove_duplicates_nostorage()
    list.print_list()


if __name__ == '__main__':
    main()
