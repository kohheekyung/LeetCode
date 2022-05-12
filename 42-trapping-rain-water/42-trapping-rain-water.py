class Solution:
    
    def trap_twopointer(self, height: List[int]) -> int:
        '''
        Runtime: 186 ms O(n)
        Memory: 15.7 MB
        '''
        # 리스트가 0이면 return 0
        if not height:
            return 0
        
        volume = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]
        
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            
            #더 높은 쪽으로 투포인터 이동
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        
        return volume
    
    def trap(self, height: List[int]) -> int:
        
        stack = []
        volume = 0
        
        for i in range(len(height)):
            
            # 변곡점을 만나는 경우 = 스택의 마지막 값과 비교
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 꺼낸다
                top = stack.pop()
            
                if not len(stack):
                    break
                
                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters
            stack.append(i)
        return volume
                
        