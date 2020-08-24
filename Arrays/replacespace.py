"""
REPLACE ALL SPACES WITH %20
"""


def replaceStringSpaces(s):
    first_pointer = 0
    result = ""

    while first_pointer < len(s):
        if s[first_pointer] == " ":
            result += "%20"
        else:
            result += s[first_pointer]
        first_pointer = first_pointer + 1

    return result


test = "Mr John Smith"
result = replaceStringSpaces(test)
print(result)
