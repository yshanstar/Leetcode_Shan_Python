__author__ = 'shye'
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTreeLevelOrderTraversal:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        res = []
        if root is None:
            return res
        nextLayer = [root]

        while len(nextLayer) != 0:
            res.append(nextLayer)

            nextLayer = []
            for node in res[-1]:
                if node.left:
                    nextLayer.append(node.left)
                if node.right:
                    nextLayer.append(node.right)
        res =[[node.val for node in layer] for layer in res]
        return res
