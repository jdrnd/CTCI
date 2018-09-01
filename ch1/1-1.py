def characters_are_unique(inputstr):
    chars = {}
    for char in inputstr:
        chars[char] = True
    return len(chars) == len(inputstr)

def characters_are_unique_nohash(inputstr):
    CHARSET_SIZE = 256
    # Assume ASCII characters
    all_chars = [0] * CHARSET_SIZE
    for char in inputstr:
        val = ord(char)
        all_chars[val] += 1
    numchars = 0
    for i in range(0, CHARSET_SIZE):
        if all_chars[i] != 0:
            numchars += 1
    return numchars == len(inputstr)


def unique_characters_test():
    print(characters_are_unique('test') == False,
        characters_are_unique('abcd') == True,
        characters_are_unique('') == True,
        characters_are_unique('&^%$$') == False
    )

def unique_characters_nohash_test():
        print(characters_are_unique_nohash('test') == False,
            characters_are_unique_nohash('abcd') == True,
            characters_are_unique_nohash('') == True,
            characters_are_unique_nohash('&^%$$') == False
        )


if __name__ == '__main__':
    unique_characters_test()
    unique_characters_nohash_test()
