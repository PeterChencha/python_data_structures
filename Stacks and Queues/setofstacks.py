class SetOfStack(object):
    STACK_LIMIT = 3
    """docstring for SetOfStack."""
    def __init__(self):
        super(SetOfStack, self).__init__()
        self.my_array = []
        self.limit = SetOfStack.STACK_LIMIT
        self.currentPointer = -1
        self.tails = []

    def push(self, data):
        if len(self.my_array) == self.limit - 1:
            self.my_array.append(data)
            self.currentPointer = self.currentPointer + 1
            self.tails.append(self.currentPointer)
            self.limit = self.limit + SetOfStack.STACK_LIMIT
        else:
            self.my_array.append(data)
            self.currentPointer = self.currentPointer + 1

    def peek(self):
        data = self.my_array[-1]
        return data

    def pop(self):
        last_item = self.my_array[-1]
        last_index = self.tails[-1]
        if self.currentPointer == last_index :
            del self.tails[-1]
            del self.my_array[-1]
            self.currentPointer = self.currentPointer - 1
        del self.my_array[-1]
        self.currentPointer = self.currentPointer - 1
        return last_item

    def peekAt(self, stack_number):
        if stack_number > len(self.tails):
            message = "Stack does not exist"
            return message
        tail_index = self.tails[stack_number-1]
        tail_data = self.my_array[tail_index]
        return tail_data

setStack = SetOfStack()
setStack.push(10)
setStack.push(25)
setStack.push(69)
setStack.push(1)
setStack.push(17)
setStack.push(967)
setStack.push(34)
print(setStack.peek())
print("Specify index", setStack.peekAt(2))
print("General Pop")
