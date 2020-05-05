class Stack(object):
    """docstring for Stack."""
    def __init__(self):
        super(Stack, self).__init__()
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        data = self.stack[-1]
        return data

    def stackSize(self):
        return len(self.stack)


test = Stack()
test.push(10)
test.push(20)
test.push(0)
test.push(1)
print('stack size:', test.stackSize())
print("Popped:", test.pop())
print("Popped:", test.pop())
print("stack size:", test.stackSize())
print("Peek:", test.peek())
print("stack size:", test.stackSize())
