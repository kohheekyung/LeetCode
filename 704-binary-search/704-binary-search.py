
class Solution:
    '''
    Binary search
    
    Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to     search target in nums. If target exist, then return its index. Otherwise, return -1
    
    Time complextity O(log N): The  ploblem divides into subproblems 
    
    
    Space complexity : O(1)  since it's a constant space solution
    

    '''
    def search(self, nums: List[int], target: int) -> int:

        # Initialize left and right pointer
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            
            # Compare middle element of the array nums[pivot] to the target value
            pivot = left + (right - left) // 2
            
            # Compare middle element of the array
            if target == nums[pivot]:
                return pivot
            # if target is smaller than the middle element
            elif target < nums[pivot]:
                right = pivot - 1
            # if target is larger than the middle element
            else:
                left = pivot + 1
        
        # Cannot find
        return -1