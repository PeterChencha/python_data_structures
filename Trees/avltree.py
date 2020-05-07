class Node(object):
    """docstring for Node."""
    def __init__(self, data):
        super(Node, self).__init__()
        self.data = data
        self.rightChild = None
        self.leftChild = None
        self.height = 0

class AVLTree(object):
    """docstring for AVLTree."""
    def __init__(self):
        super(AVLTree, self).__init__()
        self.root = None

    def insert(self, data):
        self.root = self.insertNode(data, self.root)

    def insertNode(self, data, node):
        if node is None:
            newNode = Node(data)
            return newNode

        if data < node.data:
            node.leftChild = self.insertNode(data, node.leftChild)
        else:
            node.rightChild = self.insertNode(data, node.rightChild)

        node.height = max(self.calculateHeight(node.leftChild), self.calculateHeight(node.rightChild)) + 1

        return self.settleViolation(data, node)

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
                print("Removing a node with only a rightChild")
                tempNode = node.rightChild
                del node
                return tempNode
            elif not node.rightChild:
                print(" Removing a node with only a leftChild")
                tempNode = node.leftChild
                del node
                return tempNode
            print("Removing node with both children")
            tempNode = self.getPredecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)
        #AVL SPECIFIC FUNCTIONS#
        if not node:
            return node

        node.height = max(self.calculateHeight(node.leftChild), self.calculateHeight(node.rightChild)) + 1
        balance = self.calcBalance(node)

        #LEFT LEFT HEAVY CASE
        if balance > 1 and self.calcBalance(node.leftChild) >= 0:
            return self.rotateRight(node)
        #LEFT RIGHT CASE
        if balance > 1 and self.calcBalance(node.leftChild) < 0:
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)
        #RIGHT RIGHT HEAVY CASE
        if balance < -1 and self.calcBalance(node.rightChild) <= 0:
            return self.rotateLeft(node)
        #RIGHT LEFT CASE
        if balance < -1 and self.calcBalance(node.rightChild) > 0:
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)

        return node

    def getPredecessor(self, node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild)

        return node

    def settleViolation(self, data, node):
        balance = self.calcBalance(node)

        #CASE 1 ==> LEFT HEAVY SITUATION
        if balance > 1 and data < node.leftChild.data:
            print("Left left heavy situation...")
            return self.rotateRight(node)
        #CASE 2 ==> RIGHT HEAVY SITUATION
        if balance < -1 and data > node.rightChild.data:
            print("Right right heavy situation...")
            return self.rotateLeft(node)
        #CASE 3 ==>
        if balance > 1 and data > node.leftChild.data:
            print("Left right heavy situation...")
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)
        #CASE 4 ==>
        if balance < -1 and data < node.rightChild.data:
            print("Right Left heavy situation...")
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)

        return node

    def calculateHeight(self, node):
        if not node:
            return -1
        return node.height

    #IF RETURN VALUE > 1 == LEFT HEAVY TREE --> RIGHT ROTATION
    #.......         < -1 == RIGHT HEAVY TREE -->LEFT ROTATION
    def calcBalance(self, node):
        if not node:
            return 0
        diff_in_height = self.calculateHeight(node.leftChild) - self.calculateHeight(node.rightChild)
        return diff_in_height

    def rotateRight(self, node):
        print("Performing right rotation on node {}".format(node.data))
        tempLeftChild = node.leftChild
        t = tempLeftChild.rightChild

        tempLeftChild.rightChild = node
        node.leftChild = t

        node.height = max(self.calculateHeight(node.leftChild), self.calculateHeight(node.rightChild)) + 1
        tempLeftChild.height = max(self.calculateHeight(tempLeftChild.leftChild), self.calculateHeight(tempLeftChild.rightChild)) + 1

        return tempLeftChild

    def rotateLeft(self, node):
        print("Performing left rotation on node {}".format(node.data))
        tempRightChild = node.rightChild
        t = tempRightChild.leftChild

        tempRightChild.leftChild = node
        node.rightChild = t

        node.height = max(self.calculateHeight(node.leftChild), self.calculateHeight(node.rightChild)) + 1
        tempRightChild.height = max(self.calculateHeight(tempRightChild.leftChild), self.calculateHeight(tempRightChild.rightChild)) + 1

        return tempRightChild

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self, node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)

        print("{}".format(node.data))

        if node.rightChild:
            self.traverseInOrder(node.rightChild)

testAVL = AVLTree()
testAVL.insert(1)
testAVL.insert(2)
testAVL.insert(3)
testAVL.insert(4)
testAVL.insert(5)
testAVL.insert(6)
testAVL.traverse()
testAVL.remove(4)
testAVL.traverse()
