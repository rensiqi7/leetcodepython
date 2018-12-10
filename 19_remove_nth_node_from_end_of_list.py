# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return None

        dummy = ListNode(0)
        dummy.next = head

        slow, quick = dummy, dummy

        for i in range(n):
            quick = quick.next

        while quick and quick.next:
            slow = slow.next
            quick = quick.next

        slow.next = slow.next.next

        return dummy.next

        # second trial after getting a hint from its solution.
        """
        dummy = ListNode(0)
        dummy.next = head
        target_prev = dummy
        tail = head
        dist = 0
        while tail is not None:
            if dist < n:
                tail = tail.next
                dist += 1
            else:
                target_prev = target_prev.next
                dist -= 1

        target_prev.next = target_prev.next.next
        return dummy.next
        """
