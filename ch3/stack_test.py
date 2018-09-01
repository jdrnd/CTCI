from stack import Stack

def main():
    values = Stack()
    values.push(0)
    values.push(1)
    values.push(2)
    values.push(3)
    print(values.length == 4)
    print(values.pop() == 3)
    print(values.pop() == 2)
    print(values.pop() == 1)
    print(values.pop() == 0)
    print(values.is_empty())
    print(values.pop() == None)

if __name__ == '__main__':
    main()
