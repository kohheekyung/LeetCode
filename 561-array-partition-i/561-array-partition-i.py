class Solution:
    def arrayPairSum_sort(self, nums: List[int]) -> int:
        '''
        오름차순으로 정렬하여 두개씩 짝
        
        Runtime 313 ms O(n)
        Memory 16.6 MB
        '''
        nums.sort()
        pairSum = 0
        for i in range(0, len(nums), 2):
            pairSum += nums[i]
        return pairSum
    
    def arrayPairSum(self, nums: List[int]) -> int:
        '''
        오름차순으로 정렬하여 두개씩 짝
        
        Runtime 284 ms O(n)
        Memory 16.6 MB
        '''
        return sum(sorted(nums)[::2])