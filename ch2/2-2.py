from utils import create_list

def main():
    list = create_list()

    print(list.get_n_from_last(0))
    print(list.get_n_from_last(1))
    print(list.get_n_from_last(5))
    print(list.get_n_from_last(6))

if __name__ == '__main__':
    main()
