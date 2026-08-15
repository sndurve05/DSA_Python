# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """

        if not head or not head.next:
            return True

        slow, fast = head, head

        while fast and fast.next:
            slow= slow.next
            fast = fast.next.next
        
        second_half = slow
       
        curr = second_half
        prev = None

        while curr:
            next_node = curr.next
            curr.next =prev
            prev = curr
            curr = next_node
        
        first_half = head
        second_half = prev

        while second_half:  # Corrected: Iterate and compare values
        # you cant compare just first_half == second.half , because they are the memory location. Even if they point on same object they store different address.
            if first_half.val != second_half.val: # hence by .val we compare the values
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True

