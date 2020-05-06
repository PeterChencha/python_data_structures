class Node(object):
    """docstring for Node."""
    def __init__(self, data):
        super(Node, self).__init__()
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree(object):
    """docstring for BinarySearchTree."""
    def __init__(self):
        super(BinarySearchTree, self).__init__()
        self.root = None

    def insert(self, data):
        if not self.root:
            newNode = Node(data)
            self.root = newNode
        else:
            self.insertNode(data, self.root)

    """O(logN) IF TREE IS BALANCED, OTHERWISE IT FALLS TO O(N) IN THIS CASE AVL AND RBT ARE NEEDED"""
    def insertNode(self, data, node):
        if data < node.data:
            if node.leftChild:
                self.insertNode(data, node.leftChild)
            else:
                newNode = Node(data)
                node.leftChild = newNode
        else:
            if node.rightChild:
                self.insertNode(data, node.rightChild)
            else:
                newNode = Node(data)
                node.rightChild = newNode

    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)

    def getMin(self, node):
        if node.leftChild:
            return self.getMin(node.leftChild)
        return node.data

    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)

    def getMax(self, node):
        if node.rightChild:
            return self.getMax(node.rightChild)
        else:
            return node.data

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self, node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)

        print("{}".format(node.data))

        if node.rightChild:
            self.traverseInOrder(node.rightChild)
