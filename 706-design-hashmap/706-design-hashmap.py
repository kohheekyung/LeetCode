class ListNode:
    
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
    
class MyHashMap:
    '''
    체이닝 기법으로 구현
    연결리스트 필요
    '''
    
    def __init__(self):
        # 빈 해시맵 초기화
        self.size = 1000
        self.hashmap = collections.defaultdict(ListNode)
        

    def put(self, key: int, value: int) -> None:
        #(키, 값) 해시맵에 삽입. 만약 존재하는 키라면 업데이트
        
        # 해싱을 통해 인덱스 구하기
        idx = key % self.size
        
        # 키값 해시맵에 삽입
        if self.hashmap[idx].key is None:
            self.hashmap[idx] = ListNode(key,value)
            return
        # 만약 존재하는 키라면 해당 키의 value값을 업데이트

        # 해싱키가 동일한 시작 노드 구하기
        node = self.hashmap[idx]
        while node:
            # 해당 노드의 키와 동일할때
            if node.key == key:
                node.value = value
                return 
            # 만약 다음 노드가 없다면 종료한다
            if node.next is None:
                break              
            # 다음 노드로 이동
            node = node.next
        node.next = ListNode(key,value)
        
    def get(self, key: int) -> int:
        # 해당 키를 가진 값을 조회

        # 해싱을 통해 인덱스 구하기
        idx = key % self.size
        
        # 없으면 return -1
        if self.hashmap[idx].key is None:
            return -1
        
        # 해싱키가 동일한 시작 노드 구하기
        node = self.hashmap[idx]
        while node:
            # 해당 노드의 키와 동일할때
            if node.key == key:
                return node.value    
            # 다음 노드로 이동
            node = node.next 
        return -1

    def remove(self, key: int) -> None:
        # 해당 키를 가진 값을 삭제
        
        # 해싱을 통해 인덱스 구하기
        idx = key % self.size
        
        if self.hashmap[idx].value is None:
            return 
        
        # 해싱키가 동일한 시작 노드 구하기
        node = self.hashmap[idx]
        
        # 인덱스의 첫번째 노드일때 삭제
        if node.key == key:
            self.hashmap[idx] = ListNode() if node.next is None else node.next 
            return
        
        # 첫번째 노드가 아닐때
        prev = node
        curr = node
        
        while curr:
            # 해당 노드의 키와 동일할때
            if curr.key == key:
                prev.next = curr.next # 앞의 노드의 next와 다음노드를 연결해줌
                return
            prev, curr = curr, curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)