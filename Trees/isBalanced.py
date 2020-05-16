"""IMPLEMENT FUNCTION TO FIND OUT IF A TREE IS BALANCED OR NOT"""


def calculateHeight(node):
    if node is None:
        return 0

    rightHeight = calculateHeight(node.rightChild)

    if rightHeight == -1 :
        return -1

    leftHeight = calculateHeight(node.leftChild)

    if leftHeight == -1:
        return -1

    heightDiff = leftHeight - rightHeight

    if abs(heightDiff) > 1:
        return -1

    return (max(leftHeight, rightHeight) + 1)

def isBalanced(node):

    if calculateHeight(node) == -1:
        return False
    return True
