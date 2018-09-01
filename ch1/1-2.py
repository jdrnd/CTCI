def is_permutation_of(str1, str2):
    chars1 = {}
    chars2 = {}

    # Assume values are initialized to 0
    for char in str1:
        if chars1.get(char) == None:
            chars1[char] = 1
        else:
            chars1[char] += 1
    for char in str2:
        if chars2.get(char) == None:
            chars2[char] = 1
        else:
            chars2[char] += 1

    # Ensure each letter has the same number of occurences in each string
    for key in chars1:
        # get returns none if key does not exist
        if chars1[key] != chars2.get(key):
            return False
    for key in chars2:
        # get returns none if key does not exist
        if chars2[key] != chars1.get(key):
            return False
    return True


def is_permutation_of_test():
    print(
        is_permutation_of('test', 'test') == True,
        is_permutation_of('test', 'tset') == True,
        is_permutation_of('test', 'teest') == False,
        is_permutation_of('abc', 'abcd') == False,
        is_permutation_of('abcde', 'abc') == False,
        is_permutation_of('', '') == True
    )

if __name__ == '__main__':
    is_permutation_of_test()
