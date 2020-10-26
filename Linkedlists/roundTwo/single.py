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

    def insertStart(self, data):
        newNode = Node(data)
        self.size = self.size + 1

        if self.head is None:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def insertEnd(self, data):
        newNode = Node(data)
        self.size = self.size + 1

        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head

            while currentNode.nextNode is not None:
                currentNode = currentNode.nextNode

            currentNode.nextNode = newNode

    def traverse(self):
        if self.head is None:
            print("Linkedlist is empty")

        currentNode = self.head

        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.nextNode


test = LinkedList()
test.insertStart(10)
test.insertStart(50)
test.insertStart(74)
test.insertEnd(112)
test.traverse()
