# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Time O(n) 66 ms
        Space O(1) 15.4 MB
        '''
        node, prev = head, None
        
        
        while node:
            # 현재 노드의 다음 노드 저장
            next = node.next
            # 현재 노드의 다음 노드 방향 변경
            node.next = prev
            # 포인터들 하나씩 옆으로 이동
            prev = node
            node = next
            
        return prev

            
            
            
    def reverseList_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Time O(n)
        Space O(n) n번의 재귀함수 호출
        '''
        def reverse(node: ListNode, prev: ListNode = None):
            # 마지막 노드라면 prev 연결리스트 반환
            if not node:
                return prev
            
            # 현재 노드의 다음 노드 저장
            next = node.next
            # 현재 노드의 다음 노드 방향 변경
            node.next = prev

            # 포인터들 하나씩 옆으로 이동하여 재귀 호출
            return reverse(next, node)
        
        return reverseList(head)