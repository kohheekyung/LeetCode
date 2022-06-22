class ListNode:
    # 포인터가 양옆으로 두개인 더블 연결리스트
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class MyCircularDeque:

    '''
    Deque란 Double ended Queue로 양쪽 끝을 모두 추출할 있는 큐.
    파이썬으로 collections.deque()으로 사용되며 내부적으론 연결리스트로 추상자료형의 형태로 구현되어 있음.
    
    Circular deque도 연결리스트로 구현 가능
    연결리스트로 구현시
    삽입, 삭제, 조회 전부 O(1)의 시간이 걸림
    '''
    def __init__(self, k: int):
        
        # 첫번째, 마지막 노드를 가리키 노드
        self.head = ListNode(None)
        self.tail = ListNode(None)
        
        # Circular deque의 최대 길이
        self.k = k
        
        # Circular deque의 현재 길이
        self.len = 0
        
        # 초기화를 위해 포인터가 서로를 향하게함
        self.head.right = self.tail        
        self.tail.left = self.head
        
    def _add(self, node, new):
        '''
        node : 삽입할 노드의 앞이 될 노드
        new : 삽입할 노드
        '''
        temp = node.right 
        node.right = new
        
        new.right = temp
        new.left = node
        
        temp.left = new
        
    def _delete(self, node):
        '''
        node : 제거할 노드의 앞이 될 노드
        '''
        temp = node.right.right
        
        node.right = temp
        node.right.left = node
        
        
    def insertFront(self, value: int) -> bool:
        
        if self.len == self.k :
            return False
        
        # 길이 업데이트
        self.len += 1
        
        # 삽입할 노드 생성
        new_node = ListNode(value)

        # 노드 추가
        self._add(self.head, new_node)
            
        return True 
        
    def insertLast(self, value: int) -> bool:
        
        if self.len == self.k :
            return False
        
        # 길이 업데이트
        self.len += 1
        
        # 삽입할 노드 생성
        new_node = ListNode(value)

        # 노드 추가
        self._add(self.tail.left, new_node)
    
        return True 
        
    def deleteFront(self) -> bool:
        
        if self.len == 0 :
            return False
        
        self.len -= 1
        
        # 사라질 노드의 앞노드 설정
        delete_node = self.head
        self._delete(delete_node)
    
        return True 
        
    def deleteLast(self) -> bool:
        if self.len == 0 :
            return False
        
        self.len -= 1
        
        # 사라질 노드의 앞노드 설정
        delete_node = self.tail.left.left
        self._delete(delete_node)
    
        return True 
    
    def getFront(self) -> int:
        return self.head.right.value if self.len else -1 
        

    def getRear(self) -> int:
        return self.tail.left.value if self.len else -1 
        
    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k
        

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()