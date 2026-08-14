#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ans = ListNode(0,head)
        dummy = ans

        while dummy.next and dummy.next.next:
            #If you write while dummy.next.next:, Python tries to look inside dummy.next to find its .next property. Since dummy.next is None, you are asking for None.next. This triggers a crash: AttributeError: 'NoneType' object has no attribute 'next'
            if dummy.next.val == dummy.next.next.val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next

        return ans.next