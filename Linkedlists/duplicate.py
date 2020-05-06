"""REMOVE DUPLICATES FROM AN UNSORTED LIST"""
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

    def insertAtBeginning(self, data):
        self.size = self.size + 1
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print("{}".format(actualNode.data))
            actualNode = actualNode.nextNode

    def removeDuplicates(self):
        current = second = self.head
        while current is not None:
            while second.nextNode is not None:
                if second.nextNode.data == current.data:
                    self.size = self.size - 1
                    second.nextNode = second.nextNode.nextNode
                else:
                    second = second.nextNode
            current = second = current.nextNode

    def size_0f_linkedlist(self):
        return self.size






test = LinkedList()
test.insertAtBeginning(10)
test.insertAtBeginning(20)
test.insertAtBeginning(10)
test.insertAtBeginning(50)
test.insertAtBeginning(25)
test.insertAtBeginning(20)
print("Elements:", test.traverseList())
print("size:", test.size_0f_linkedlist())
test.removeDuplicates()
print("Elements:", test.traverseList())
print("size:", test.size_0f_linkedlist())
