class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BalancedBinaryTree:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        return False if self.checkHeight(root) == -1 else True

    def checkHeight(self, root):
        if root is None:
            return 0
        leftHeight = self.checkHeight(root.left)
        if leftHeight == -1:
            return -1

        rightHeight = self.checkHeight(root.right)
        if rightHeight == -1:
            return -1

        if abs(leftHeight - rightHeight) > 1:
            return -1

        return max(leftHeight, rightHeight) + 1

