def construct_charmap(str1):
    chars = {}
    for char in str1:
        if chars.get(char) == None:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars
