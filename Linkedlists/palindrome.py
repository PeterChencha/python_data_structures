import math

class Node(object):
    """docstring for Node."""
    def __init__(self, data):
        super(Node, self).__init__()
        self.data = data
        self.nextNode = None


class LinkedListDivide(object):
    """docstring forLinkedListDivide."""
    def __init__(self):
        super(LinkedListDivide, self).__init__()
        self.head = None
        self.head2 = None
        self.size = 0

    def insertStart(self, data):
        self.size = self.size + 1
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def reverseLinkedList(self, node):

        if node is None or node.nextNode is None:
            return

        currentNode = node
        previous = None

        while currentNode is not None:
            temp = currentNode
            currentNode = currentNode.nextNode
            temp.nextNode = previous
            previous = temp
        node = previous

    def splitLinkedListAt(self, location):

        if self.head.nextNode is None or location <= 0:
            return

        count = 1
        currentNode = self.head

        while count != location:
            currentNode = currentNode.nextNode
            count = count + 1
        if currentNode.nextNode is None:
            return
        else:
            self.size = location
            self.head2 = currentNode.nextNode
            currentNode.nextNode = None

    def isPalindrome(self):
        if self.head is None:
            return

        splitAt = math.ceil((self.size/2)) + 1

        self.splitLinkedListAt(splitAt)

        firstCurrenNode = self.head
        secondCurrentNode = self.head2
        print("Before reverse")
        print(firstCurrenNode.data)
        print(secondCurrentNode.data)

        if splitAt > self.size/2:
            self.reverseLinkedList(secondCurrentNode)
        elif splitAt < self.size/2:
            self.reverseLinkedList(firstCurrenNode)
        else:
            self.reverseLinkedList(firstCurrenNode)
        print("After reverse")
        print(firstCurrenNode.data)
        print(secondCurrentNode.data)
        while firstCurrenNode is None or secondCurrentNode is None:
            if firstCurrenNode.data == secondCurrentNode.data:
                firstCurrenNode = firstCurrenNode.nextNode
                secondCurrentNode = firstCurrenNode.nextNode
            else:
                message = "Not Palindrome"
                return message
        message = "Is Palindrome"
        return message


    def traverseList(self):

        actualNode = self.head

        while actualNode is not None:
            print("{}".format(actualNode.data))
            actualNode = actualNode.nextNode

    def traverseSplitList(self):
        if self.head2 is None:
            return

        actualNode = self.head2

        while actualNode is not None:
            print("{}".format(actualNode.data))
            actualNode = actualNode.nextNode


    def size_0f_linkedlist(self):
        return self.size

test = LinkedListDivide()
test.insertStart(20)
test.insertStart(10)
test.insertStart(13)
test.insertStart(55)
test.insertStart(75)
print("Original list before split")
test.traverseList()
print(test.isPalindrome())
#TEST SPLITTING
# test = LinkedListDivide()
# test.insertStart(20)
# test.insertStart(10)
# test.insertStart(13)
# test.insertStart(55)
# test.insertStart(75)
# print("Original list before split")
# test.traverseList()
# print("size of original before split:", test.size_0f_linkedlist())
# test.splitLinkedListAt(3)
# print("Splited list")
# test.traverseSplitList()
# print("Original list after split")
# test.traverseList()
# print("size of original list after split:", test.size_0f_linkedlist())
