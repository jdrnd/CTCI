def is_rotation_of(str1, str2):
    if len(str1) != len(str2):
        return False

    # Adding a string back to back will make the unroateted word appear continously in the total string
    str1 += str1
    return str2 in str1

def is_rotation_of_test():
    print(
        is_rotation_of('erbottlewat', 'waterbottle') == True,
        is_rotation_of('test', 'ttes') == True
    )

if __name__ == '__main__':
    is_rotation_of_test()
