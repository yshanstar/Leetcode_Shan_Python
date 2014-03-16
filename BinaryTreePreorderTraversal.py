from Ulti import *
class BinaryTreePreorderTraversal:
    def preorderTraversal(self, root):
        res = []
        if root is None:
            return res

        stack = [root]
        while stack:
            root = stack.pop()
            res.append(root.val)

            if root.right:
                stack.append(root.right)

            if root.left:
                stack.append(root.left)

        return res

mySolution = BinaryTreePreorderTraversal()
root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
root.left = node1
root.right = node2

res = mySolution.preorderTraversal(root)
print ( res )


