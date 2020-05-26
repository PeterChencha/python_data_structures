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
        self.status = True

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


    def is_balanced_tree(self):
        if self.root:
            self.isBalancedInOrder(self.root)

    def isBalancedInOrder(self, node):
        if node.rightChild is None or node.leftChild is None:
            return

        if node.rightChild.data < node.data:
            self.status = False
            return self.status
        if node.leftChild.data > node.data:
            self.status = False
            return self.status

        if node.leftChild:
            self.isBalancedInOrder(node.leftChild)
        if node.rightChild:
            self.isBalancedInOrder(node.rightChild)
        print("status:", self.status)
        return self.status

    # def is_tree(self):
    #     comparitor = self.root.data
    #     actual_node = self.root
    #     check_root = self.compare_subtree(self.root)
    #     if check_root is True:
    #         print("In the first check")
    #         while actual_node.leftChild is not None:
    #             if self.has_child(actual_node.leftChild):
    #                 left_check = self.compare_subtree(actual_node.leftChild)
    #                 if left_check is True:
    #                     if actual_node.leftChild.rightChild is not None:
    #                         if comparitor > actual_node.leftChild.rightChild.data:
    #                             actual_node = actual_node.leftChild
    #                         else:
    #                             return False
    #                 else:
    #                     print("I am the culprit", left_check)
    #                     return False
    #         while actual_node.rightChild is not None:
    #             if self.has_child(actual_node.rightChild):
    #                 right_check = self.compare_subtree(actual_node.rightChild)
    #                 if right_check is True:
    #                     if actual_node.rightChild.leftChild is not None:
    #                         if comparitor < actual_node.rightChild.leftChild.data:
    #                             actual_node = actual_node.rightChild
    #                         else:
    #                             return False
    #                 else:
    #                     return False
    #
    #         return True
    #     else:
    #         return False
    #
    # def compare_subtree(self, node):
    #     if node.data > node.leftChild.data and node.data < node.rightChild.data:
    #         return True
    #     else:
    #         return False
    #
    # def has_child(self, node):
    #     print("Has child")
    #     if node.rightChild is not None or node.leftChild is not None:
    #         return True
    #     return False



bst = BinaryTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(6)
bst.traverse()
print("Is Binary Tree", bst.is_balanced_tree())
