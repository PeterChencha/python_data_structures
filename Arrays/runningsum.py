def runningSum(testArray):
    #CHECK IF ONLY HAS ONE VALUE
    if len(testArray) < 2:
        return testArray

    pointer = 1
    sum = testArray[0]

    while pointer < len(testArray):
        sum = sum + testArray[pointer]
        testArray[pointer] = sum
        pointer = pointer + 1

    return testArray

test = [3,1,2,10,1]
result = runningSum(test)
print(result)
