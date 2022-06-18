class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Time O(n) 1240 ms
        Memory O(n) 24.6 MB
        '''
        stack = [] # 인덱스 저장
        result = [0] * len(temperatures) # 다음 날짜까지의 날 수 저장
        
        for i, curr_temperature in enumerate(temperatures):
            # 스택에 담긴날의 온도와 현재 온도와 비교하여 현재 온도가 더 높다면
            while stack and temperatures[stack[-1]] < curr_temperature:
                # 스택의 인덱스와 현재 인덱스의 차를 결과에 저장 
                last_idx = stack.pop()
                result[last_idx] = i - last_idx
             
            # 현 인덱스 저장
            stack.append(i)
        return result