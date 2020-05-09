def isPalindrome(data):

    if len(data) == 0:
        message = "Data is empty"
        return message

    start = 0
    end = len(data) - 1

    while start < end:
        if data[start] == data[end]:
            start = start + 1
            end = end - 1
        else:
            message = "Not palindrome"
            return message
    message = "Data elements is a palindrome"
    return message

data = [3, 1, 3]
data1 = [3, 1, 4]
data2 = [9, 1, 0, 1, 9]
data3 = ['kayak']
data4 = ["check"]
test = isPalindrome(data3)

print(test)
