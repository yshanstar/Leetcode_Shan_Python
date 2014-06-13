class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.rgiht = None

class PathSum:
	# @param root, a tree node
   	# @param sum, an integer
   	# @return a boolean
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        if root.left is None and root.right is None:
            return (root.val == sum)

        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

