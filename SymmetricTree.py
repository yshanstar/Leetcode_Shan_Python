class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SymmetricTree:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root is None:
            return True
        elif root.left is None and root.right is None:
            return True

        return self.checkSym(root.left, root.right)

    def checkSym(self, left, right):
        if left == right == None:
            return True

        if not (left and right):
            return False

        if left.val != right.val:
            return False

        return self.checkSym(left.left, right.right) and self.checkSym(left.right, right.left)

