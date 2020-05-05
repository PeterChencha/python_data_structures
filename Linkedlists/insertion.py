class Node(object):
    """docstring for Node."""
    def __init__(self, data):
        super(Node, self).__init__()
        self.data = data
        self.nextNode = None

class LinkedList(object):
    """docstring for LinkedList."""
    def __init__(self):
        super(LinkedList, self).__init__()
        self.head = None
        self.size = 0

    """O(1) TIME COMPLEXITY"""
    def insertStart(self, data):
        self.size = self.size + 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    """ O(N) TIME COMPLEXITY"""
    def insertEnd(self, data):
        self.size = self.size + 1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    def remove(self, data):
        #FIRST CHECK IF EMPTY
        if self.head is None:
            return
        self.size = self.size - 1
        currentNode = self.head
        previousNode = None;

        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode

        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode



    """O(N)"""
    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print("{}".format(actualNode.data))
            actualNode = actualNode.nextNode


    def size(self):
        return self.size

test = LinkedList()
test.insertStart(20)
test.insertEnd(50)
test.insertStart(10)
test.remove(20)
print(test.traverseList())