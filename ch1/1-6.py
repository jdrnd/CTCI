def basic_compression(str1):

    curr_char = ''
    count = 0
    compressed_str = []

    for char in str1:
        if char != curr_char:
            if curr_char != '':
                compressed_str.append(curr_char)
                compressed_str.append(str(count))
            curr_char = char
            count = 1
        else:
            count += 1

    compressed_str.append(curr_char)
    compressed_str.append(str(count))

    compressed_str = ''.join(compressed_str)

    if len(compressed_str) < len(str1):
        return compressed_str
    else:
        return str1

def basic_compression_test():
    print(
        basic_compression('test') == 'test',
        basic_compression('teeeeeeest') == 't1e7s1t1',
        basic_compression('eeeee') == 'e5',
        basic_compression('abcdefg') == 'abcdefg',
        basic_compression('aaabaaa') == 'a3b1a3'
    )

if __name__ == '__main__':
    basic_compression_test()
