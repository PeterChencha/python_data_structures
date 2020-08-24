def longestPrefix(strs):
    first_string = strs[0]
    second_string = strs[1]
    third_string = strs[2]

    for i in first_string:
        print(i)


test_strs = ["flower", "flow", "flight"]
result = longestPrefix(test_strs)
print(result)
