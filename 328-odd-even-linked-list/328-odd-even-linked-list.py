# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Time O(n) 62 ms
        Space O(1) 16.6 MB n의 크기에 관계없이 항상 변수개수가 일관성있다
        
        홀짝 노드를 각각 구성한 다음 홀수 노드의 마지막에 짝수 노드를 이어주면 된다.
        '''
        if head is None:
            return None
        
        odd = head
        even = head.next
        even_head = head.next
        
        while even and even.next :
        
            # 홀수번째만 연결
            odd.next = odd.next.next
            odd = odd.next
            
            # 짝수번째만 연결 
            even.next = even.next.next
            even = even.next
            
        #홀수 노드의 마지막에 짝수 노드 연결
        odd.next = even_head
        
        return head