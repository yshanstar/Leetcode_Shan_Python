class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedListCycle:
    def hasCycle(self, head):
        if (head is None) or (head.next is None):
            return False

        slow = head
        fast = head

        while (fast is not None) and (fast.next is not None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if fast is None or fast.next is None:
            return False

        return True




