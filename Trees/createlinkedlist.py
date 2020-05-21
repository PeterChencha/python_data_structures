"""In a Binary Tree, Create Linked Lists of all the nodes at each depth."""

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

    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print("{}".format(actualNode.data))
            actualNode = actualNode.nextNode

class BinaryNode(object):
    """docstring for BinaryNode."""
    def __init__(self, data):
        super(BinaryNode, self).__init__()
        self.data = data
        self.leftChild = None
        self.rightChild = None


class BinaryTree(object):
    """docstring for BinaryTree."""
    def __init__(self):
        super(BinaryTree, self).__init__()
        self.root = None

    def insert(self, data):
        if not self.root:
            newNode = BinaryNode(data)
            self.root = newNode
        else:
            self.insertNode(data, self.root)

    def insertNode(self, data, node):

        if data < node.data:
            if node.leftChild:
                self.insertNode(data, node.leftChild)
            else:
                newNode = BinaryNode(data)
                node.leftChild = newNode
        if data > node.data:
            if node.rightChild:
                self.insertNode(data, node.rightChild)
            else:
                newNode = BinaryNode(data)
                node.rightChild = newNode

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self, node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)
        print("{}".format(node.data))

        if node.rightChild:
            self.traverseInOrder(node.rightChild)


    def treeDepth(self, node):
        if node is None:
            return 0
        if node.rightChild is None and node.leftChild is None:
            return 1
        else:
            right_depth = 1 + self.treeDepth(node.rightChild)
            left_depth = 1 + self.treeDepth(node.leftChild)

            if right_depth > left_depth:
                return right_depth
            else:
                return left_depth

class SplitTreeToLinkedList(object):
    """docstring for SplitTreeToLinkedList."""
    def __init__(self):
        super(SplitTreeToLinkedList, self).__init__()
        self.lists = {}

    def split(self, tree, depth):
        depth = depth
        if self.lists.get(depth) == None:
            linkedList = LinkedList()
            linkedList.insertStart(tree.data)
            self.lists[depth] = linkedList
        else:
            linkedList = self.lists.get(depth)
            linkedList.insertStart(tree.data)
            self.lists[depth] = linkedList

        if tree.leftChild:
            self.split(tree.leftChild, depth - 1)
        if tree.rightChild:
            self.split(tree.rightChild, depth - 1)
        return self.lists

    def traverseGeneratedLists(self):

        count = 1

        while self.lists.get(count) != None:
            list = self.lists[count]
            actualNode = list.head
            print("LinkedLists")
            while actualNode is not None:
                print("{}".format(actualNode.data))
                actualNode = actualNode.nextNode
            count = count + 1


bst = BinaryTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(6)
bst.traverse()
print("Depth", bst.treeDepth(bst.root))
depth = bst.treeDepth(bst.root)
algorithm = SplitTreeToLinkedList()
algorithm.split(bst.root, depth)
algorithm.traverseGeneratedLists()
