from utils import create_list

def main():
    list = create_list()

    print(list.print_list())

    middle_node = list._get_node_by_index(3)
    list.delete_middle_node(middle_node)
    list.print_list()

if __name__ == '__main__':
    main()
