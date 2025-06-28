# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return None

        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        
        removeNextIndex = length - n - 1
        if removeNextIndex == -1:
            return head.next

        removeNext = head
        for i in range(removeNextIndex):
            removeNext = removeNext.next
        removeNext.next = removeNext.next.next

        return head