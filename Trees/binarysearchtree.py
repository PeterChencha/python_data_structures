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

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    def removeNode(self, data, node):
        if not node:
            return node

        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)
        else:

            if not node.leftChild and not node.rightChild:
                print("Removing a leaf node")
                del node
                return None
            if not node.leftChild:
                print("Removing a node with single rightChild")
                tempNode = node.rightChild
                del node
                return tempNode
            elif not node.rightChild:
                print("Removing node with single leftChild")
                tempNode = node.leftChild
                del node
                return tempNode
            print("Removing node with both children")
            tempNode = self.getPredecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)

        return node

    def getPredecessor(self, node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild)

        return node

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

bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(6)

print("Min value:",bst.getMinValue())
bst.traverse()
bst.remove(5)
bst.traverse()
print("Min value:",bst.getMinValue())
