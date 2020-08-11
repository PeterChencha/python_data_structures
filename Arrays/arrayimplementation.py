class MyArray(object):
    def __init__(self):
        self.length = 0
        self.data = {}

    def checkIfEmpty(self):
        if self.length == 0:
            return True

    def get(self, index):
        return self.data[index]

    def random(self):
        return (" This is a random string ")

    def add(self, value):
        self.data[self.length] = value
        self.length = self.length + 1

    def removeFirstValue(self):
        if self.checkIfEmpty():
            error = "Array is empty"
            return error
        else:
            firstItem = self.data[0]
            del self.data[0]
            self.length = self.length - 1
            return firstItem

    def removeLastValue(self):
        #COMMONLY REFERED TO AS POP
        if self.checkIfEmpty():
            error = "Array is empty"
            return error
        else:
            lastItem = self.data[self.length - 1]
            del self.data[self.length - 1]
            self.length = self.length - 1
            return lastItem

    def deleteSpecific(self, index):
        item = self.data[index]
        self.shiftItems(index)
        return item

    def shiftItems(self, index):
        for _ in range(index, (self.length - 1)):
            self.data[_] = self.data[_ + 1]
        del self.data[self.length - 1]
        self.length = self.length - 1


arr = MyArray()
arr.add(70)
arr.add(50)
arr.add(100)
#print (arr.random())
#print (arr.get(2))
#print(arr.removeLastValue())
#print(arr.removeFirstValue())
print (arr.deleteSpecific(1))
print (arr.length)
