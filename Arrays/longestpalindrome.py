def isPalindrome(data):
    start = 0
    end = len(data) - 1

    while start < end :
        if data[start] != data[end]:
            return False
        else:
            start = start + 1
            end = end - 1

    return True

def sub_string(data, start, end):
    return data[start:end + 1]

def longestPalindrome(data):
    max = 0
    count = 0
    string = ""
    for i in range(len(data)):
        start = i
        end = len(data)
        moving = i

        while moving < end :
            subString = sub_string(data,start,moving)
            if isPalindrome(subString):
                count = len(sub_string(data,start,moving))
                if count > max :
                    max = count
                    string = subString
            moving = moving + 1

    return string

test = 'cbbd'
result = longestPalindrome(test)
print(result)
