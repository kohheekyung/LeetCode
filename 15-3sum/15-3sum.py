class Solution:
    def threeSum_Bruteforce(self, nums: List[int]) -> List[List[int]]:
        ''' 
        Time Limit Exceeded O(n^3)
        '''
        result = []
        
        # 앞뒤로 같은 값이 있을 경우 이를 쉽게 처리하기 위해 sort
        nums.sort()
        
        for i in range(len(nums)):
            
            #  만약 앞뒤 수가 동일하다면
            if i>0 and nums[i] == nums[i-1]:
                continue
        
            for j in range(i+1, len(nums)):
                
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                
                for k in range(j+1, len(nums)):
                    
                    if k>j+1 and nums[k] == nums[k-1]:
                        continue
                    
                    if nums[i]+nums[j]+nums[k] == 0:
                        result.append([nums[i],nums[j],nums[k]])
        
        return result
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ''' 
        Two point 
        
        '''
        result = []
        
        # 앞뒤로 같은 값이 있을 경우 이를 쉽게 처리하기 위해 sort
        nums.sort()
        
        for i in range(len(nums)-2):
            
        
            #  만약 앞뒤 수가 동일하다면
            if i>0 and nums[i] == nums[i-1]:
                continue
                
            left, right = i+1, len(nums) - 1
    
    
            while left < right :
    
    
                three_sum = nums[i] + nums[left] + nums[right]
        
                if three_sum < 0 :
                    left += 1
                elif three_sum > 0:
                    right-=1
                else:
                    result.append([nums[i],nums[left],nums[right]])
        

                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right-=1
                        
        return result
        