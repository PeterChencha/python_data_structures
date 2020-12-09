def removeDuplicates(data):
    currentPointer = 0
    count = 0
    indexes = []

    while len(data) > currentPointer + 1:
        if data[currentPointer] == data[currentPointer + 1]:
            if count == 0:
                indexes.append(currentPointer)
                indexes.append(currentPointer + 1)
                count = count + 2
            else:
                indexes.append(currentPointer + 1)
                count = count + 1

        else:
            count = 0

        currentPointer = currentPointer + 1

    if len(indexes) > 0:
        while len(indexes) > 0:
            i = indexes.pop()
            del data[i]

    return data


duplicates = [1, 2, 8, 8, 8, 9, 12, 12, 13]
result = removeDuplicates(duplicates)
print(result)
