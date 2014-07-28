__author__ = 'shye'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class ConvertSortedListtiBinarySearchTree:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        num = []
        cur = head
        while cur is not None:
            num.append(cur.val)
            cur = cur.next

        return self.createBST(num, 0, len(num)-1)

    def createBST(self, num, start, end):
        if start > end:
            return None
        mid = (end + start)/2
        root = TreeNode(num[mid])
        root.left = self.createBST(num, start, mid-1)
        root.right = self.createBST(num, mid+1, end)
        return root


