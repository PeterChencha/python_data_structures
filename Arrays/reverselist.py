"""REVERSE A LIST EG [1, 10, 11, 4] ==> [4, 11, 10. 1]"""

def reverseList(data):
    new_array = []
    while len(data) != 0 :
        last_value = data[-1]
        new_array.append(last_value)
        data.remove(last_value)
    return new_array

print(reverseList([1, 10, 11, 4]))

"""REVERSE IN PLACE"""

def reverseInPlace(data):

    start = 0
    end = len(data) - 1

    while start < end :
        temp = data[start]
        data[start] = data[end]
        data[end] = temp
        start = start + 1
        end = end - 1

    return data

print("Using In place algorithm")
print(reverseInPlace([1, 10, 11, 4, 77]))
#print(reverseInPlace("OAK"))
