class TreeNode:
    def __init__(self, x)
        self.val = x
        self.left = None
        self.right = None

class SumRootToLeafNumbers:
    def sumNumbers(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val

        SumRootToLeafNumbers.res = 0
        if root.left:
            self.getSum(root.left, root.val)

        if root.right:
            self.getSum(root.right, root.val)

        return SumRootToLeafNumbers.res

    def getSum(self, root, valueParent):
        if root is None:
            return

        if (root.left is None) and (root.right is None):
            SumRootToLeafNumbers.res += (10 * valueParent + root.val)

        self.getSum(root.left, 10 * valueParent + root.val)
        self.getSum(root.right, 10 * valueParent + root.val)

