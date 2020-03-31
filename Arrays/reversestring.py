def reverseString(string):
    backward = []
    for _ in reversed(range(len(string))):
        backward.append(string[_])
    return ' '.join(backward)

test_string = "Hi my name is Peter"
results = reverseString(test_string)
print results
