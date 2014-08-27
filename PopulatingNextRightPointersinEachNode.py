__author__ = 'shye'
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class PopulatingNextRightPointersinEachNode:
    # @Param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None or (root.left is None and root.right is None):
            return
        if root.left is not None:
            root.left.next = root.right
        if root.right is not None:
            if root.next:
                root.right.next = root.next.left
            else:
                root.right.next = None
        self.connect(root.left)
        self.connect(root.right)