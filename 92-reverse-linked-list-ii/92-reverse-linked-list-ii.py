# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        '''The idea is simple and intuitive: find linkedlist [m, n], reverse it, then connect m with n+1, connect n with m-1'''
        
        if not head or left == right:
            return head
 

        root = ListNode(0)
        root.next = head
        pre = root

        # left 이전 노드까지 이동
        for i in range(left - 1):
            pre = pre.next
        
    
        # left, right 사이값 revese
        reverse = None
        curr = pre.next
        for _ in range(right - left + 1):

            next = curr.next
            curr.next = reverse
            reverse = curr
            curr = next
        #[dummy .... pre]    [reverse,..., pre.next]   [curr .....]
        
        pre.next.next = curr
        pre.next = reverse

  
    
        return root.next
            