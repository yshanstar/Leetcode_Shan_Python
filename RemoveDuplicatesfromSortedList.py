class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class RemoveDuplicatesfromSortedList:
    def deleteDuplicates(self, head):
        if head is None:
            return None

        num = []
        cur = head
        nextAvail = cur
        while cur.next != None:
            if cur.val != cur.next.val:
                nextAvail.next = cur.next
                nextAvail = nextAvail.next
            cur = cur.next

        nextAvail.next = None
        return head
