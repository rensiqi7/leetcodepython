# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        start = ListNode(0)
        start.next = head
        move = start
        while move is not None and move.next is not None:
            temp = move.next
            while temp.next is not None and temp.val == temp.next.val:
                temp = temp.next
            if temp != move.next:
                move.next = temp.next
            else:
                move = temp
        return start.next
