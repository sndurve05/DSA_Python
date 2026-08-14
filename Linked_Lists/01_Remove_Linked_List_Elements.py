# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        ans = ListNode(0,head) #ans stores a permanent bookmark to the very first dummy node so you never lose the entrance to your list.
        dummy = ans #dummy stores a temporary tracking address that constantly updates to show which node the computer is currently inspecting.
        '''
        Both ans and dummy are pointers. They do not store the entire list or the actual node data directly. Instead, they store a memory address (a reference) that points to a specific ListNode object in your computer's memory.'''

        while dummy:
            while dummy.next and dummy.next.val == val:
                dummy.next = dummy.next.next
            dummy = dummy.next

        return ans.next


'''
initially
 ans ──┐
       ├─> [ Node 0 ] ──> [ Node 6 ] ──> [ Node 3 ] ──> None
dummy ──┘




Rewiring the Pointer
 ans ──┐
       ├─> [ Node 0 ] ───────────────> [ Node 3 ] ──> None
dummy ──┘            \                 /
                      ──> [ Node 6 ] ┘  (Disconnected!)

                      
                      
                      
                      
Moving dummy Forward

 ans ──────> [ Node 0 ] ───────────────> [ Node 3 ] ──> None
                                           ▲
dummy ─────────────────────────────────────┘
'''