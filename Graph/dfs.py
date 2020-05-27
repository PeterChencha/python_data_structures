""" NOTE DONT RUN BOTH RECURSIVE AND ITERATIVE TOGETHER CAUSE THE ALL NODES WILL
BE MARKED VISITED BY THE FIRST TO RUN"""
class Node(object):
    """docstring for Node."""
    def __init__(self, name):
        super(Node, self).__init__()
        self.name = name
        self.adjacencyList = []
        self.visited = False
        self.predecessor = None

class DepthFirstSearch(object):
    """docstring for DepthFirstSearch."""

    def dfs(self, node):
        node.visited = True
        print("{}".format(node.name))

        for n in node.adjacencyList:
            if not n.visited:
                self.dfs(n)

    def dfs_iterative(self, node):
        stack = []
        stack.append(node)

        while stack:
            actualNode = stack.pop()
            if not actualNode.visited:
                print('{}'.format(actualNode.name))
                actualNode.visited = True

            for n in actualNode.adjacencyList:
                if not n.visited:
                    stack.append(n)


node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")

node1.adjacencyList.append(node2)
node1.adjacencyList.append(node3)
node2.adjacencyList.append(node4)
node4.adjacencyList.append(node5)

dfsInstance = DepthFirstSearch()
dfsInstance.dfs(node1)
print('Using dfs_iterative')
dfsInstance.dfs_iterative(node1)
