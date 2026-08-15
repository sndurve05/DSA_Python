# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy1 = list1
        dummy2 = list2

        ans = ListNode()
        ans.next = None
        ans.head = None
        answer = ans
        while dummy1 or dummy2 :
            while dummy1 and dummy2 and dummy1.val >= dummy2.val:
                ans.next = dummy2
                dummy2 = dummy2.next
                ans = ans.next

            while dummy1 and dummy2 and dummy1.val < dummy2.val:
                ans.next = dummy1
                dummy1 = dummy1.next
                ans = ans.next

            while dummy2 and not dummy1:
                ans.next = dummy2
                dummy2 = dummy2.next
                ans = ans.next

            while dummy1 and not dummy2:
                ans.next = dummy1
                dummy1 = dummy1.next
                ans = ans.next         
 
        return answer.next
