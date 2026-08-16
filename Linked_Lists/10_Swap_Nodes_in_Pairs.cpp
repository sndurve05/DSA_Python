// # Definition for singly-linked list.
// # class ListNode(object):
// #     def __init__(self, val=0, next=None):
// #         self.val = val
// #         self.next = next
// class Solution(object):
//     def swapPairs(self, head):
//         """
//         :type head: Optional[ListNode]
//         :rtype: Optional[ListNode]
//         """
//         temp = head
//         if not head or not head.next:
//             return head

//         temp = head.next
//         head.next = self.swapPairs(temp.next)
//         temp.next = head

//         return temp

        



 // Definition for singly-linked list.
 struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
  };
 
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (!head || !head->next){
            return head;
        }
        ListNode* temp = head->next;
        head->next = swapPairs(temp->next);
        temp->next = head;
        return temp;
    }
};