class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            
            # get middle position
            pivot = left + (right - left) // 2
            
            if nums[pivot] == target :
                return pivot
            elif nums[pivot] < target:
                left = pivot + 1
            else:
                right = pivot - 1
                
        return left 
   