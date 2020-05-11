class MultipleStacks(object):
    """docstring for MultipleStacks."""
    def __init__(self):
        super(MultipleStacks, self).__init__()
        self.my_array = []
        self.top = {}
        self.last = {}
        self.currentPointer = 0

    def insert(self, stack_number, stack_data):

        if stack_number in self.top.keys():
            self.my_array.append(stack_data)
            self.last[stack_number] = self.currentPointer
            self.currentPointer = self.currentPointer + 1
        else:
            self.my_array.append(stack_data)
            self.top[stack_number] = self.currentPointer
            self.currentPointer = self.currentPointer + 1

    def peek(self, stack_number):
        if stack_number in self.last.keys():
            index = self.last[stack_number]
            data = self.my_array[index]
            return data
        message = "Stack does not exist"
        return message

    def traverseStacks(self):
        for _ in self.my_array:
            print(_)

test = MultipleStacks()
test.insert(1, 10)
test.insert(1, 20)
test.insert(1, 30)
test.insert(2, 55)
test.insert(3, 3)
test.insert(3, 99)
test.insert(2, 30)
test.insert(3, 25)
test.insert(1, 300)
test.traverseStacks()
print("Peek first stack:", test.peek(1))
print("Peek second stack:", test.peek(2))
print("Peek third stack:", test.peek(3))
print("Peek non existent stack:", test.peek(10))
