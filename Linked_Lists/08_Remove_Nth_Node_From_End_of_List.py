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

        #Imagine two people walking. Person A starts walking and gets a head start of meters. Then Person B starts walking at the same speed. When Person A hits the wall at the end of the hallway, Person B is exactly meters away from that wall.

        slow = head  
        fast = head
        count = 0 
        while fast and count != n:
            fast = fast.next
            count+=1
        if not fast:
            return head.next
        
        while fast.next: # slow should be one node before the target
            slow = slow.next 
            fast = fast.next

        slow.next = slow.next.next
        return head
