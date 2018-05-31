# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        l3 = result
        flag = 0
        while (1):
            if (not l1 and l2):
                temp = l2.val + flag
                l2 = l2.next
            elif (l1 and not l2):
                temp = l1.val + flag
                l1 = l1.next
            elif (not l1 and not l2 and flag):
                temp = flag
                result.val = temp
            else:
                temp = l1.val + l2.val + flag
                l1 = l1.next
                l2 = l2.next

            flag = 0
            if (temp > 9):
                temp -= 10
                flag = 1

            result.val = temp
            if (not l1 and not l2 and not flag):
                break
            result.next = ListNode(0)
            result = result.next
        return l3
