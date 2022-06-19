class MyCircularQueue:
    # 원형 큐 구현
    def __init__(self, k: int):

        self.q = [None] * k # 리스트 활용하여 원형 큐 구현
        self.maxlen = k # 원형 큐의 최대 길이 
        
        self.p1 = 0 # front 포인터
        self.p2 = 0 # rear 포인터

    
    
    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None:
            # rear 포인터인 p2의 위치에 값을 삽입
            self.q[self.p2] = value
            # p2 포인터 위치 한 칸 이동 하지만 나머지 연산을 통해 전체 길이에서 벗어나지 안도록함
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False 

    def deQueue(self) -> bool:
        # 제거하고자 하는 front 포인터에 값이 없으면 False
        if self.q[self.p1] is None:
            return False
        else:
            # front 포인터 위치 값을 None으로 변경
            self.q[self.p1] = None
            # P1 포인터 위치 한 칸 이동 하지만 나머지 연산을 통해 전체 길이에서 벗어나지 안도록함
            self.p1 = (self.p1 + 1) % self.maxlen
            return True

    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self) -> int:
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]

    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()