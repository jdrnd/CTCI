def urlify(str,):
    REPLACE_CHAR = '%20'
    new_chars = []
    for char in str:
        if char == ' ':
            new_chars.append(REPLACE_CHAR)
        else:
            new_chars.append(char)
    return ''.join(new_chars)


def urilfy_test():
    print(
        urlify('test') == 'test',
        urlify('te st') == 'te%20st',
        urlify(' ') == '%20',
        urlify('test statement and things') == 'test%20statement%20and%20things'
    )


if __name__ == '__main__':
    urilfy_test()
