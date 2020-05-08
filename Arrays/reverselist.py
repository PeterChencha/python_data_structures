"""REVERSE A LIST EG [1, 10, 11, 4] ==> [4, 11, 10. 1]"""

def reverseList(data):
    new_array = []
    while len(data) != 0 :
        last_value = data[-1]
        new_array.append(last_value)
        data.remove(last_value)
    return new_array

print(reverseList([1, 10, 11, 4]))

"""CAN JUST USE list.reverse()"""
# def reverseList(data):
#     new_array = []
#
#     if len(data) == 0:
#         return
#
#     # if len(data) > 0:
#     #     last_value = data[-1]
#     #     new_array.append(last_value)
#     #     data.remove(last_value)
#     #     print(new_array)
#     #     reverseList(data)
#
#     last_value = data[-1]
#     new_array.append(last_value)
#     data.remove(last_value)
#     print(new_array)
#     reverseList(data)
