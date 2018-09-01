from linked_list import LinkedList

# takes an int as a list of values to create a list from
def create_list(values):
    values = [int(x) for x in str(values)]
    list = LinkedList(values[0])

    for i in range(1, len(values)):
        list.insert_at_end(values[i])
    return list
