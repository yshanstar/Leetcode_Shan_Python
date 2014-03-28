class TreeNode:
    def __init__(self, x):
        self.val = x
        self.lelf = None
        self.right = None

class MaximumDepthofBinaryTree:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root is None:
            return 0
        if root is not None and root.left is None and root.right is None:
            return 1
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
