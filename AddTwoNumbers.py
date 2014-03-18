class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class AddTwoNumbers:
    def addTwoNumbers(self, l1, l2):
        if l1 is None and l2 is None:
            return None

        if l1 is None:
            return l2

        if l2 is None:
            return l1

        carry = 0
        head = ListNode(0);
        cur = head

        while l1 and l2:
            sumValue = l1.val + l2.val + carry
            carry = sumValue / 10
            cur.next = ListNode(sumValue % 10)
            l1 = l1.next
            l2 = l2.next
            cur = cur.next

        while l1:
            sumValue = l1.val + carry
            carry = sumValue / 10
            cur.next = ListNode(sumValue % 10)
            cur = cur.next
            l1 = l1.next

        while l2:
            sumValue = l2.val + carry
            carry = sumValue / 10
            cur.next = ListNode(sumValue % 10)
            cur = cur.next
            l2 = l2.next

        if carry > 0:
            cur.next = ListNode(carry)

        return head.next

