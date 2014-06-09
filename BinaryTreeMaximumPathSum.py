__author__ = 'yshan_000'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTreeMaximumPathSum:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return root.val

        BinaryTreeMaximumPathSum.total = -100000
        self.maxSum(root)

        return BinaryTreeMaximumPathSum.total


    def maxSum(self, root):
        if root is None:
            return 0

        # init
        total = root.val
        lmax = 0
        rmax = 0

        if root.left:
            lmax = self.maxSum(root.left)
            if lmax > 0:
                total = lmax + total

        if root.right:
            rmax = self.maxSum(root.right)
            if rmax > 0:
                total = rmax + total

        if total > BinaryTreeMaximumPathSum.total: BinaryTreeMaximumPathSum.total = total

        return max(root.val, (root.val + lmax), (root.val + rmax))

