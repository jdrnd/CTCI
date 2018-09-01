from queue import Queue

def main():
    values = Queue()
    values.add(0)
    values.add(1)
    values.add(2)
    values.add(3)
    print(values.peek() == 0)
    print(values.length == 4)
    print(values.pop() == 0)
    print(values.pop() == 1)
    print(values.pop() == 2)
    print(values.pop() == 3)
    print(values.is_empty())

if __name__ == '__main__':
    main()
