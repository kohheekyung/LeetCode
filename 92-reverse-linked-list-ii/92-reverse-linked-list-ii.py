# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        '''
        Time O(n)
        Space O(1)
        '''
        
        if not head or left == right:
            return head
 

        root = ListNode(0)
        root.next = head
        start = root

        # left 이전 노드까지 이동
        for i in range(left - 1):
            start = start.next
        end = start.next
        
        # 반대로 변환
        for _ in range(right - left ):
            tmp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = tmp
        
        return root.next
            