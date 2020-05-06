"""WRITE ALGORITHM TO FIND THE Kth TO LAST ELEMENT OF A SINGLY LINKED LIST"""

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
        self.size = self.size + 1
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def size_0f_linkedlist(self):
        return self.size

    def getFromLast(self, pointer):
        if self.head is None:
            return
        elif pointer > self.size:
            error = "Invalid Pointer"
            return error

        no_of_nexts = self.size - pointer
        actualNode = self.head
        while no_of_nexts != 1:
            actualNode = actualNode.nextNode
            no_of_nexts = no_of_nexts - 1
        value = actualNode.data
        message = " The {} from last is {}".format(pointer, value)
        return message

    """O(N)"""
    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print("{}".format(actualNode.data))
            actualNode = actualNode.nextNode


test = LinkedList()
test.insertStart(1)
test.insertStart(3)
test.insertStart(4)
test.insertStart(13)
test.insertStart(12)
test.traverseList()
print("size:", test.size_0f_linkedlist())
print(test.getFromLast(2))
