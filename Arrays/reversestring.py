def reverseString(string):
    backward = []
    for _ in reversed(range(len(string))):
        backward.append(string[_])
    return ' '.join(backward)

# test_string = "Hi my name is Peter"
# results = reverseString(test_string)
# print results

def reverseBySlicing(string):
    len_of_string = len(string)
    slicedString = string[len_of_string::-1]
    return slicedString

test_string = "Hi my name is Peter"
results = reverseBySlicing(test_string)
print results
