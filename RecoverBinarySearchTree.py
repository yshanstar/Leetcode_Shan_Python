__author__ = 'shye'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class RecoverBinarySearchTree:
    #@param root, a tree node
    #@return a tree node
    def recoverTree(self, root):
        if root is None or (root.left is None and root.right is None):
            return root
        self.n1 = self.n2 = None
        self.prev = None
        self.findTwoNodes(root)
        self.n1.val, self.n2.val = self.n2.val, self.n1.val
        return root

    def findTwoNodes(self, root):
        if root:
            self.findTwoNodes(root.left)
            if self.prev and self.prev.val > root.val:
                self.n2 = root
                if self.n1 is None:
                    self.n1 = self.prev
            self.prev = root
            self.findTwoNodes(root.right)