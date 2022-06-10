# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        root = head
        while head and head.next:
            
            first_val = head.val
            second_val = head.next.val

            head.val = second_val
            head.next.val = first_val
            
            head = head.next.next
            
        return root
        