"""
PERFORM BASIC STRING COMPRESSION USING THE COUNTS OF REPEATED CHARACTERS.
"""


def compressString(string):
    pointer = 0
    count = 1
    result = ""

    while pointer < len(string) - 1:
        if string[pointer] == string[pointer + 1]:
            count = count + 1
        else:
            result += string[pointer] + str(count)
            count = 1
            reset_point = pointer
            print("Pointer:{}".format(pointer))
        pointer = pointer + 1

    if reset_point != pointer:
        diff = (pointer - reset_point)
        result += string[pointer] + str(diff)

    return result


test = "aabcccccaaabbb"
result = compressString(test)
print(result)
