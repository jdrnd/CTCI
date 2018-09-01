def is_permutation_of_palindrome(input_str):
    chars = {}
    for char in input_str:
        # Ignore spaces
        if char != ' ':
            if chars.get(char) == None:
                chars[char] = 1
            else:
                chars[char] += 1

    # Al palodroms will only have 1 at max character with an odd number of occurences
    odd_char_found = False
    for char in chars:
        if chars[char] % 2 != 0:
            if odd_char_found:
                return False
            else:
                odd_char_found = True
    return True


def is_permutation_of_palindrome_test():
    print(
        is_permutation_of_palindrome('test') == False,
        is_permutation_of_palindrome('teest') == True,
        is_permutation_of_palindrome('race car') == True,
        is_permutation_of_palindrome('bb') == True,
        is_permutation_of_palindrome('test-set') == False
    )

if __name__ == '__main__':
    is_permutation_of_palindrome_test()
