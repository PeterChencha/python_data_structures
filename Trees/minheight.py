"""GIVEN AN ASCENDING ARRAY WITH UNIQUE CHARACTERS CREATE A BINARY TREE WITH MINIMAL HEIGHT"""
import math

class Node(object):
    """docstring for Node."""
    def __init__(self, data):
        super(Node, self).__init__()
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree(object):
    """docstring for BinarySearchTree."""
    def __init__(self, arrayList):
        super(BinarySearchTree, self).__init__()
        self.arrayList = arrayList
        self.root = None
        self.mid = len(self.arrayList)/2
        self.right = self.mid + 1
        self.left = self.mid - 1

    def insert(self):
        while self.right != len(self.arrayList):
            if self.root is None:
                newNode = Node(self.arrayList[self.mid])
                self.root = newNode
            else:
                self.insertNode(self.root)

    def insertNode(self, node):
        if self.arrayList[self.left] < node.data :
            if node.leftChild:
                self.insertNode(node.leftChild)
            else:
                newNode = Node(self.arrayList[self.left])
                node.leftChild = newNode
                print("Left pointer", self.left)
                self.left = self.left - 1
        else:
            if node.rightChild:
                self.insertNode(node.rightChild)
            else:
                newNode = Node(self.arrayList[self.right])
                node.rightChild = newNode
                print("Right pointer", self.right)
                self.right = self.right + 1

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self, node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)

        print("{}".format(node.data))

        if node.rightChild:
            self.traverseInOrder(node.rightChild)

my_array = [4, 7, 9, 12, 19]

bst = BinarySearchTree(my_array)

bst.insert()
bst.traverse()
