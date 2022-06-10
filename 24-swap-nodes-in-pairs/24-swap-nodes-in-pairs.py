# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs_value(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        root = head
        while head and head.next:
            
            first_val = head.val
            second_val = head.next.val

            head.val = second_val
            head.next.val = first_val
            
            head = head.next.next
            
        return root
    
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Time O(n)
        Space O(1)
        '''
        root = prev = ListNode(0)
        prev.next = head 
        
        while head and head.next:
            
            # b가 head를 가리키고 head가 b 다음 노드를 가리키도록함
            # b가 앞에 있는 것으로 위치 변경
            b = head.next
            head.next = b.next
            b.next = head
            
            # prev가 b를 가리키도록함
            prev.next = b
            
            # 다음번 비교를 위해 이동
            head = head.next
            prev = prev.next.next
            
            
        return root.next
    
    def swapPairs_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Time O(n)
        Space O(n)
        '''
        if head and head.next:
            prev = head.next
            # 스왑된 값 리턴받음
            head.next = self.swapPairs_recursive(prev.next)
            prev.next = head
            return prev
            
        return head