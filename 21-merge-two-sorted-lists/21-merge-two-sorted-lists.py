# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Time O(n)
        Memory O(1)
        '''
        if list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2
        elif not list1 and not list2:
            return None
        
        head = ListNode(-1)
        prev = head

        # 둘 다 None이 아닐 동안
        while list1 and list2:
            # list1의 값이 더 작으면 prev의 다음 값에 list1 연결하고 list1 업데이트
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            # list2의 값이 더 작으면 prev의 다음 값에 list2 연결하고 list2 업데이트
            else:
                prev.next = list2
                list2 = list2.next
            # prev 이동
            prev = prev.next
        
        # 남은 연결리스트 붙이기
        if list1 is not None:
            prev.next = list1
        else:
            prev.next = list2
            
        return head.next
                