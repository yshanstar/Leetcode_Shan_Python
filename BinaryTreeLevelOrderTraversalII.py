class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTreeLevelOrderTraversalII:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        res = []
        if root is None:
            return res

        curLevel = []
        nextLevel = []
        curVals = []
        curLevel.append(root)

        while curLevel:
            node = curLevel.pop(0)
            curVals.append(node.val)

            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)

            if not curLevel:
                res.append(curVals)
                curLevel = nextLevel
                nextLevel = []
                curVals = []

        return res[::-1]

node1 = TreeNode(1)
node2 = TreeNode(2)
node1.left = node2

test = BinaryTreeLevelOrderTraversalII()
res = test.levelOrderBottom(node1)
