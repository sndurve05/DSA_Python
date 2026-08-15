# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        #using the commutative property and adding the length of list so that we get the common starting together after one full addition of lengths of both lists.

        #Make each pointer walk A + B; the unequal parts cancel, so they meet at the shared node.
        a = headA
        b = headB

        while a != b: # we dont do a.val != b.val because intersection has the exact same node, not 2 different nodes with same value.
        # for example, in example 1 l1 = 4,1,8,4,5 and l2 = 5,6,1,8,4,5 here intersection is at 8 not 1 even if the value is same.
            a = a.next if a else headB
            b = b.next if b else headA

        return a