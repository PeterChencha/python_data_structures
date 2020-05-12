class MinStack(object):
    """docstring for MinStack."""
    def __init__(self):
        super(MinStack, self).__init__()
        self.array = []
        self.minPointer = []
        self.currentPointer = -1

    def isEmptyStack(self):

        return self.array == []

    def insert(self, data):

        if self.isEmptyStack():
            self.array.append(data)
            self.currentPointer = self.currentPointer + 1
            self.minPointer.append(self.currentPointer)
        elif data < self.array[self.minPointer[-1]]:
            self.array.append(data)
            self.currentPointer = self.currentPointer + 1
            self.minPointer.append(self.currentPointer)
        else:
            self.array.append(data)
            self.currentPointer = self.currentPointer + 1

    def pop(self):
        if self.isEmptyStack():
            message = "Stack is empty"
            return message

        last_item = self.array[-1]
        min_index = self.minPointer[-1]

        if last_item == self.array[min_index]:
            self.currentPointer = self.currentPointer - 1
            del self.minPointer[-1]
            del self.array[-1]
            return last_item
        else:
            self.currentPointer = self.currentPointer - 1
            del self.array[-1]
            return last_item

    def minItem(self):
        if self.isEmptyStack():
            message = "Stack is empty"
            return message

        min_index = self.minPointer[-1]
        min_item = self.array[min_index]

        return min_item


    def traverseStack(self):

        if self.isEmptyStack():
            message = "Stack is empty"
            return message
        print("Items")
        for item in range(self.currentPointer+1):
            data = self.array[item]
            print(data)


minstack = MinStack()
minstack.insert(0)
minstack.insert(5)
minstack.insert(1)
minstack.insert(3)
minstack.insert(2)
minstack.traverseStack()
print("Min Item", minstack.minItem())
print("poped element:", minstack.pop())
minstack.traverseStack()
