class BinaryNode(object):
    """docstring for BinaryNode."""
    def __init__(self, data):
        super(BinaryNode, self).__init__()
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.visited = False


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

    def traverseWithBFS(self):
        queue = []
        queue.append(self.root)
        self.root.visited = True

        while queue:
            actualNode = queue.pop(0)
            print(actualNode.data)

            if actualNode.leftChild is not None and not actualNode.leftChild.visited:
                actualNode.leftChild.visited = True
                queue.append(actualNode.leftChild)

            if actualNode.rightChild is not None and not actualNode.rightChild.visited:
                actualNode.rightChild.visited = True
                queue.append(actualNode.rightChild)

    def traversePre(self):
        if self.root:
            self.traverseInPreOrder(self.root)

    def traverseInPreOrder(self, node):
        print('{}'.format(node.data))

        if node.leftChild:
            self.traverseInPreOrder(node.leftChild)

        if node.rightChild:
            self.traverseInPreOrder(node.rightChild)

    def traversePost(self):
        if self.root:
            self.traverseInPostOrder(self.root)

    def traverseInPostOrder(self, node):

        if node.leftChild:
            self.traverseInPostOrder(node.leftChild)

        if node.rightChild:
            self.traverseInPostOrder(node.rightChild)

        print('{}'.format(node.data))




bst = BinaryTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(6)
bst.insert(4)
bst.traverse()
print("Using bfs")
bst.traverseWithBFS()
print('Using DFS Preorder')
bst.traversePre()
print('Using DFS Postorder')
bst.traversePost()
