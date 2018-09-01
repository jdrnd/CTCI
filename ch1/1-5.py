from helpers import construct_charmap

def is_one_edit_away(str1, str2):
    str1hash = construct_charmap(str1)
    str2hash = construct_charmap(str2)

    # More than one character inserted or removed
    if abs(len(str1) - len(str2)) > 1: return False

    # A character was inserted or deleted
    elif abs(len(str1) - len(str2)) == 1:
        single_difference_found = False

        # Itterate through each character that appears
        for char in str1hash:
            if str1hash[char] != str2.count(char):
                if abs(str1.count(char) - str2.count(char)) == 1 and not single_difference_found:
                    single_difference_found = True
                else: return False

        for char in str2hash:
            if str2hash[char] != str2.count(char):
                if abs(str1.count(char) - str2.count(char)) == 1 and not single_difference_found:
                    single_difference_found = True
                else: return False
    # Both strings have same length, check for replaced character
    else:
        replace_found = False
        for i in range(0, len(str1)):
            if str1[i] != str2[i]:
                if replace_found: return False
                else: replace_found = True

    return True


def is_one_edit_away_test():
    print(
        is_one_edit_away('pale', 'ple') == True,
        is_one_edit_away('pales', 'pale') == True,
        is_one_edit_away('pale', 'bale') == True,
        is_one_edit_away('pale', 'bake') == False,
        is_one_edit_away('joel', 'joeel') == True,
        is_one_edit_away('joel', 'joe') == True,
        is_one_edit_away('test', 'qesq') == False 
    )

if __name__ == '__main__':
    is_one_edit_away_test()
