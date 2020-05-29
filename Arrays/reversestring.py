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


def reverseStringUsingStack(string):
    len_of_string = len(string)
    stack = []

    for i in range(len_of_string):
        stack.append(string[i])

    result = ""

    for i in range(len_of_string):
        result += stack.pop()

    return result

print("Testing using iteration")
test_string = "Hi my name is Peter"
results = reverseStringUsingStack(test_string)
print results
