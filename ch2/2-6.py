from linked_list import LinkedList
from utils import create_list
from math import ceil

def is_palindrome(list):
    start = list.head
    end = list.tail

    pairs = ceil(list.get_length() / 2) # Nummber of times we need to check pairs of values
    for _ in range(0, pairs):
        if start.get_value() == end.get_value():
            start = start.next
            end = end.prev
        else:
            return False
    return True

def main():
    print("Test")
    print(is_palindrome(create_list(100)) == False)
    print(is_palindrome(create_list(6852)) == False)
    print(is_palindrome(create_list(88)) == True)
    print(is_palindrome(create_list(0)) == True)
    print(is_palindrome(create_list(101)) == True)


if __name__ == '__main__':
    print('test')
    main()
