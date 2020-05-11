"""IMPLEMENTATION OF TERNARY SEARCH TREE"""

class Node(object):
    """docstring for Node."""
    def __init__(self, character):
        super(Node, self).__init__()
        self.character = character
        self.leftNode = None
        self.middleNode = None
        self.rightNode = None
        self.value = 0

class TST(object):
    """docstring for TST."""
    def __init__(self):
        super(TST, self).__init__()
        self.rootNode = None

    def put(self, key, value):
        self.rootNode = self.putValue(self.rootNode, key, value, 0)

    def putValue(self, node, key, value, index):

        char = key[index]

        if node == None:
            node = Node(char)

        if char < node.character:
            node.leftNode = self.putValue(node.leftNode, key, value, index)
        elif char > node.character:
            node.rightNode = self.putValue(node.rightNode, key, value, index)
        elif index < len(key) - 1:
            node.middleNode = self.putValue(node.middleNode, key, value, index+1)
        else:
            node.value = value

        return node

    def get(self, key):

        node = self.getItem(self.rootNode, key, 0)

        if node == None:
            message = "Key does not exist"
            return message

        return node.value

    def getItem(self, node, key, index):

        if node == None:
            return None

        c = key[index]

        if c < node.character:
            return self.getItem(node.leftNode, key, index)
        elif c > node.character:
            return self.getItem(node.rightNode, key, index)
        elif index < len(key) - 1:
            return self.getItem(node.middleNode, key, index+1)
        else:
            return node

tst = TST()

tst.put("apple", 100)
tst.put("flowers", 10)
tst.put("juice", -500)
print(tst.get("peter"))
