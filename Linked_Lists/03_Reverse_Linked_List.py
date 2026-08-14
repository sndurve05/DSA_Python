# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head 

        while curr:
            next_node = curr.next # this is the track of the actual next node in the linked list; as later on we change it to prev, we are storing it in a temporary variable.
            curr.next = prev  #"Change the direction that curr is pointing. Break its forward link, turn it around, and make it point backward to prev."
            prev = curr #this is a relocation step. It does not alter any nodes or arrows. It simply shifts our tracking label forward so we are ready for the next step.
            curr = next_node #relocation step, tracks forward setting curr to the next node in the linked list.

        return prev


