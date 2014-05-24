__author__ = 'yshan_000'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class InsertionSortList:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head is None or head.next is None:
            return head

        node = head

        while node.next is not None:
            cur = node.next

            if cur.val >= node.val:
                node = node.next
                continue

            node.next = cur.next

            if cur.val <= head.val:
                cur.next = head
                head = cur
                continue

            pos = self.findInsertionPos(head, cur)

            cur.next = pos.next
            pos.next = cur

        return head

    def findInsertionPos(self, head, node):
        pos = head
        while head is not None and node.val > head.val:
            pos = head
            head = head.next

        return pos