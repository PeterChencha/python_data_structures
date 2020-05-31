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

    def mergeUsingMergeSort(self, node=self.head):
        if node == None or node.next == None:
            return node

        middle_node = self.findMiddleNode(node)
        second_head = middle_node.nextNode

        middle.next = None

        left_half = mergeUsingMergeSort(node)
        right_half = mergeUsingMergeSort(second_head)

        sorted_list = self.mergelist(left_half, right_half)
        return sorted_list

    def findMiddleNode(self, node):
        current = node
        following = node

        while following.nextNode.nextNode is not None:
            current = currentNode.nextNode
            following = following.nextNode.nextNode

        return current

    def mergelist(self, left_half, right_half):
        pass


    def sortLinkedList(self):
    """USING SELECTION SORT"""
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
test.insertStart(50)
test.insertStart(10)
print("Before Sort")
print(test.traverseList())
test.sortLinkedListBubble()
print("After sort")
print(test.traverseList())
print("Size of linked list")
print(test.size_0f_linkedlist())
