# Definition for singly-linked list.

# This is a straight forward approach of counting all the nodes 
# and then traversing till the middle node.
#however it takes extra space and an additional traversal.

'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        count = 0
        while curr:
            count+=1
            curr= curr.next
       

        mid = (count//2) + 1
        count = 0
        curr = head
        
        while count != mid-1:
            print(curr)
            curr = curr.next
            count+=1
            
        return curr

        '''



# A faster approach is to use two pointer as slow and fast, 
# where slow travels one step and fast travels 2 steps, by the time 
# fast reaches the end, slow reaches the middle of the linkded list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
         