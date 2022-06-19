class MyQueue:
    # 스택을 이용하여 큐 구현
    def __init__(self):
        # 스택 두개 구현
        self.input = []
        self.output = []
       
    def push(self, x: int) -> None:
        # 큐의 마지막에 삽입
        self.input.append(x)

    def pop(self) -> int:
        # 큐의 처음의 값을 반환 및 제거
        # peek을 통해 output 정리
        self.peek()
        
        # output의 마지막값 반환 및 제거
        return self.output.pop()
        
    def peek(self) -> int:
        # 큐의 처음의 값을 조회
        
        # output이 비었으면 모두 재입력
        if not self.output:
            # input에서 꺼내서 output에 담음
            while self.input:
                self.output.append(self.input.pop())
        # output의 마지막값 반환
        return self.output[-1]

    def empty(self) -> bool:
        # 큐가 비었는지 확인
        return self.input == [] and self.output == []
        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()