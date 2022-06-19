class MyStack:
    '''
    큐로 LIFO 스택을 구현하는 문제
    '''
    def __init__(self):
        # 데크 사용
        self.q = collections.deque()
        
    def push(self, x: int) -> None:
        # 스택의 맨위에 삽입  
        
        # 큐의 맨뒤에 삽입 후
        self.q.append(x)
        # 큐의 앞의 값들을 뒤로 옮겨줌
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        # 스택의 맨위의 값 반환
        return self.q.popleft()
        

    def top(self) -> int:
        # 스택의 맨위의 값 조회
        return self.q[0]

    def empty(self) -> bool:
        # 스택이 비었는지 확인
        return len(self.q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()