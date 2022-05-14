class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        '''
        오름차순으로 정렬하여 두개씩 짝
        '''
        nums.sort()
        
        pairSum = 0
        for i in range(0, len(nums), 2):
            pairSum += nums[i]
            
        return pairSum