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

    """O(N)"""
    def remove(self, data):
        #FIRST CHECK IF EMPTY m
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


    def sortLinkedList(self):

        actualNode = self.head
        checkNode = None

        if actualNode is None:
            return

        while actualNode is not None:
            checkNode = actualNode.nextNode
            while checkNode is not None:
                if actualNode.data > checkNode.data:
                    tempdata = actualNode.data
                    actualNode.data = checkNode.data
                    checkNode.data = tempdata
                checkNode = checkNode.nextNode
            actualNode = actualNode.nextNode


    def find(self, value):

        if self.head is None:
            message = "LinkedList is empty"
            return message

        currentNode = self.head

        while currentNode is not None:
            if currentNode.data == value:
                message = "{} was found in the LinkedList".format(value)
                return message
            elif currentNode.nextNode is None:
                message = "{} was NOT found in the LinkedList".format(value)
                return message
            currentNode = currentNode.nextNode

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
        message = "The {} from last is {}".format(pointer, value)
        return message
    

    """O(N)"""
    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print("{}".format(actualNode.data))
            actualNode = actualNode.nextNode


    def size_0f_linkedlist(self):
        return self.size

test = LinkedList()
test.insertStart(20)
test.insertEnd(50)
test.insertStart(10)
test.insertStart(13)
test.insertStart(55)
test.remove(20)
print(test.traverseList())
print(test.size_0f_linkedlist())
print(test.find(100))
