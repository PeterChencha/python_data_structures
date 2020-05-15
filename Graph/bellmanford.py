import sys

class Node(object):
    """docstring for Node."""
    def __init__(self, name):
        super(Node, self).__init__()
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacenciesList = []
        self.minDistance = sys.maxsize

class Edge(object):
    """docstring for Edge."""
    def __init__(self, weight, startVertex, targetVertex):
        super(Edge, self).__init__()
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex

class BellmanFordAlgorithm(object):
    """docstring for BellmanFordAlgorithm."""
    def __init__(self, arg):
        super(BellmanFordAlgorithm, self).__init__()
        self.arg = arg
