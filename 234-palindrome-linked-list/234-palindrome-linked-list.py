# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
       def isPalindrome_deque(self, head: ListNode) -> bool:
            '''
            
            Time : O(n) 910 ms
            Memory : O(1)  47.4 MB
            '''
            q = collections.deque()
            
            if not head:
                return True
            
            node = head
            
            #리스트 변환
            while node is not None:
                q.append(node.val)
                node = node.next
                
            # 팰린드롬 판별
            while len(q) > 1:
                if q.popleft() != q.pop():
                    return False
            
            return True
    
       def isPalindrome(self, head: ListNode) -> bool:
            '''
            
            Time : O(n) 910 ms
            Memory : O(1)  47.4 MB
            '''
            rev = None
            slow = fast = head
            
            #런너를 이용해 역순 연결 리스트 구성
            while fast and fast.next:
                fast = fast.next.next # fast 런너는 두칸씩
                rev, rev.next, slow = slow, rev, slow.next # slow 런너는 한칸씩 이동, rev.next에 rev저장하여 역순으로 계속 새로운 노드 추가
            
            # 홀수일 경우 위의 while문을 통해 fast는 마지막에 None이 아니고, slow는 중앙에 위치
            # 홀수일 경우 중앙값은 고려를 하지 않아 한칸 옆으로 이동해주어야함
            if fast:
                slow = slow.next

            #팰린드롬 여부 확인
            # 정상적으로 종료된다며 slow와 rev 전부 None 될 것이다.
            while rev and rev.val == slow.val:
                slow, rev = slow.next, rev.next
            
            return not rev
                
        