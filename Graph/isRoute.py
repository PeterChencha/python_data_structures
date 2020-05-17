"""GIVEN A DIRECTED GRAPH, WRITE ALGORITHM TO FIND OUT IF THERE IS A ROUTE BETWEEN TWO NODES"""
def depthFirstTraversal(node):
    node.visited = True

    for n in node.adjacentNodes:
        if not n.visited:
            depthFirstTraversal(n)

def breathFirstTraversal(node):
    queue = []
    queue.append(node)
    node.visited = True

    while queue:
        actualNode = queue.pop(0)

        for n in actualNode.adjacentNodes:
            if not n.visited:
                n.visited = True
                queue.append(n)

def isRoute(startNode, targetNode):

    depthFirstTraversal(startNode)

    if not targetNode.visited:
        return False
    return True
