# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    우선순위 큐는 우선순위가 높은 순으로 값을 추출하는 자료구조.
    정렬 알고리즘에 의해 삽입, 삭제 시간이 의존될 수 있음.
    
    해당 문제는 우선순위 큐(힙)으로 풀면 쉽게 풀이 가능.
    
    Time: O(Nlogk)우선순의 큐는 이진트리의 형태를 가짐으로 삽입시 O(log k)시간이 걸리고 조회시 O(1)시간이 걸림 
    k는 연결리스트의 개수,N은 output 연결리스트의 노드 개수
    
    Space : O(n) output 연결리스트의 노드 개수, 힙사이즈 O(k)이나 N보다 대체적으로 적음
    
    
    '''
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        root = result = ListNode(None)
        heap = []
        
        # 각 연결리스트의 루트를 힙에 저장
        for i in range(len(lists)):
            if lists[i]:
                # heapq는 minheap을 지원하여 lists[i].val이 작은 순서대로 pop할 수 있다
                # 튜플의 첫번째 원소가 작은 순으로 정렬하며, 첫번째 원소가 같을 경우 두번째 원소로 비교 
                in_tuple = (lists[i].val, i ,lists[i])
                heapq.heappush(heap, in_tuple)
                
        while heap:
            # 가장 값이 작은 노드의 연결리스트 부터 나오게 된다. 
            out_tuple  = heapq.heappop(heap) 
            
            idx = out_tuple[1]
            result.next = out_tuple[2] # 연결리스트를 result노드와 연결
            
            # result 연결된 연결리스트에 다음 값이 있을 경우 그 다음 값을 다시 힙에 넣어준다
            
            result = result.next 
            if result.next:
                in_tuple = (result.next.val, idx , result.next)
                heapq.heappush(heap, in_tuple)
                
        return root.next
                
            