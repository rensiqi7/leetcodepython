# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # T: O(n+m) S: O(1)
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None

        pA = headA
        pB = headB

        lenA = 0
        while pA is not None:
            pA = pA.next
            lenA += 1

        lenB = 0
        while pB is not None:
            pB = pB.next
            lenB += 1

        pA = headA
        pB = headB
        if lenA > lenB:
            for i in range(lenA - lenB):
                pA = pA.next

        else:
            for i in range(lenB - lenA):
                pB = pB.next

        while pA != pB:
            pA = pA.next
            pB = pB.next

        return pA
