class Node(object):
    """docstring for Node."""
    def __init__(self, data):
        super(Node, self).__init__()
        self.data = data
        self.nextNode = None
        self.previousNode = None

class DoubleLinkedList(object):
    """docstring for DoubleLinkedList."""
    def __init__(self):
        super(DoubleLinkedList, self).__init__()
        self.head = None
        self.size = 0

    def insertStart(self, data):
        self.size = self.size + 1
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            self.head.previousNode = newNode
            newNode.nextNode = self.head
            self.head = newNode

    """O(N)"""
    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print("{}".format(actualNode.data))
            actualNode = actualNode.nextNode

test = DoubleLinkedList()
test.insertStart(10)
test.insertStart(30)
print(test.traverseList())
