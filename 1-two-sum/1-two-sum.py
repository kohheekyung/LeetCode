class Solution:
    
    def twoSum_bruteforce(self, nums: List[int], target: int) -> List[int]:
        '''
        Runtime: 4500 ms
        Memory: 14.9 MB
        '''
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in nums[i+1:]:
                return [i, nums[i+1:].index(complement) + (i+1)]
            
