class LeftRotate(object):
    def __init__(self, array, multiple):
        self.array = array
        self.multiple = multiple

    def checkIfEmpty(self):
        if len(self.array) == 0:
            return True


    def removeFirstValue(self):
        if self.checkIfEmpty():
            error = "Array is empty"
            return error
        else:
            firstItem = self.array[0]
            del self.array[0]
            return firstItem

    def addLastItem(self):
        #COMMONLY REFERED TO AS POP
        if self.checkIfEmpty():
            error = "Array is empty"
            return error
        else:
            lastItem = self.removeFirstValue()
            self.array.append(lastItem)
        return self.array

    def leftRotateArray(self):
        count = 0
        while self.multiple > count:
            self.addLastItem()
            count = count + 1

        return self.array

test_arr = [1,2,3,4,5]
multiple = 4
my_array = LeftRotate(test_arr, multiple)
result = my_array.leftRotateArray()
print(result)
