# def inf_string(a, b):
#     if len(a) > len(b):
#         return False
#
#     if len(a) == 0 or len(b) == 0:
#         return False
#
#     i = 0
#     counter = 0
#
#     while i < len(a):
#         if a[counter] == b[counter]:
#             counter = counter + 1
#         else:
#             return False
#         i = i + 1
#
#     return True
#
#
# testSting = "abcd"
# testInfinite = "abce"
# result = inf_string(testSting, testInfinite)
# print(result)


def inf_string(a, b):
    multiplier = 5
    a = a * multiplier

    if a in b:
        return 1
    else:
        return 0


testSting = "abcd"
testInfinite = "abcdabcdabcdabcdabcdabcd"
result = inf_string(testSting, testInfinite)
print(result)
