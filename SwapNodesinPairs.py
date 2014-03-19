class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class SwapNodesinPairs:
    def swapPairs(self, head):
        if head is None:
            return None

        if head.next is None:
            return head

        helper = ListNode(0)
        helper.next = head

        prev = helper
        cur = head

        while (cur is not None) and (cur.next is not None):
            tmp = cur.next.next
            cur.next.next = prev.next
            prev.next = cur.next
            cur.next = tmp
            prev = cur
            cur = prev.next


        return helper.next

