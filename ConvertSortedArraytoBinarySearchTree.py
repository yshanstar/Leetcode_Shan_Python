__author__ = 'shye'
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ConvertSortedArraytoBinarySearchTree:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        return createBST(num, 0, len(num)-1)

    def createBST(self, num, start, end):
        if start > end:
            return None
        mid = (end + start)/2
        root = TreeNode(num[mid])
        root.left = self.createBST(num, start, mid-1)
        root.right = self.createBST(num, mid+1, end)
        return root