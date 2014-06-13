class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class PathSumII:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if root is None:
            return []
        PathSumII.res = []
        PathSumII.sum = sum
        self.getPath(root, [root.val], root.val)

        return PathSumII.res

    def getPath(self, root, valList, currSum):
        if root.left is None and root.right is None:
            if currSum == PathSumII.sum:
                PathSumII.res.append(valList)
                return

        if root.left:
            self.getPath(root.left, valList + [root.left.val], currSum + root.left.val)

        if root.right:
            self.getPath(root.right, valList + [root.right.val], currSum + root.right.val)
