__author__ = 'yshan_000'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class SortList:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head is None or head.next is None:
            return head

        fast = head
        slow = head

        while fast.next is not None:
            fast = fast.next.next
            if fast is None:
                break
            slow = slow.next

        right = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(right)

        return self.mergeTwoList(left, right)

    def mergeTwoList(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        node = None
        head = None

        while (l1 is not None) and (l2 is not None):
            if l1.val <= l2.val :
                if node is None:
                    node = l1
                    head = node
                else:
                    node.next = l1;
                    node = node.next
                l1 = l1.next
            else:
                if node is None:
                    node = l2
                    head = node
                else:
                    node.next = l2
                    node = node.next
                l2 = l2.next

        if l1 is not None:
            node.next = l1
        elif l2 is not None:
            node.next = l2

        return head