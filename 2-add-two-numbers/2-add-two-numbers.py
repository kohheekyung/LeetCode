# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Time O(max(m,n)) 95 ms
        Space O(max(m,n)) 13.9 MB
        '''
        
        root = head = ListNode(0)
        
        carry = 0
        while l1 or l2 or carry > 0:
            
            val = 0
            if l1 :
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            val += carry
            
            # carry, ramain = dimod(val,10)
            carry = val // 10
            remain = val % 10
            
            head.next = ListNode(remain)
            head = head.next
            
        return root.next