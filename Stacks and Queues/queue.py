class Queue(object):
    """docstring for Queue."""
    def __init__(self):
        super(Queue, self).__init__()
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        data = self.queue[0]
        return data

    def queueSize(self):
        return len(self.queue)

test = Queue()
test.enqueue(10)
test.enqueue(20)
test.enqueue(30)
print("Size:", test.queueSize())
print("Dequeue:", test.dequeue())
print("Size:", test.queueSize())
print("Peek:", test.peek())
print("Size:", test.queueSize())
