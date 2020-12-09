def removeDuplicate(data):

    count = 0
    indexes = []

    for i in range(len(data)-1):
        for j in range(i+1, len(data)):
            if data[i] == data[j]:
                count = count + 1
                indexes.append(j)

    if len(indexes) > 0:
        initial = len(indexes)
        while len(indexes) > 0:
            if initial == len(indexes):
                i = indexes.pop()
                del data[i]
            else:
                i = indexes.pop()
                i = i - 1
                del data[i]

    return data


duplicates = [13, 9, 5, 9, 1, 13]
duplicates2 = [13, 9, 1, 4, 9]
duplicates3 = [13, 12, 13, 9, 1, 9, 5]
result = removeDuplicate(duplicates2)
print(result)
