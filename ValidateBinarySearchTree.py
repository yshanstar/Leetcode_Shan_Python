class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ValidateBinarySearchTree:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        minV = -2147483648
        maxV = 2147483647
        return self.isValidBSTImpl(root, minV, maxV)

    def isValidBSTImpl(self, root, min, max):
        if root is None:
            return True

        return root.val > min and root.val < max and self.isValidBSTImpl(root.left, min, root.val) and self.isValidBSTImpl(root.right, root.val, max)
