class Solution:
    '''
    Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
    '''
    def sortedSquaresBruteForce(self, nums: List[int]) -> List[int]:
        
        '''
        [Time exceed solution]
        Time complexity O(NlogN)
        Space complexity O(N) -> python list.sort 
        '''
        
        return sorted(n *n for n in nums)
    
    
    
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        '''
        [Accepted]
        Time complexity O(N)
        Space compextiy O(N) if return, O(1) if print
        '''
        
        # Initialize two pointers and sorted list
        left, right = 0, len(nums) -1
        sortedSquares = [0] * len(nums)
        
        # Inverse loop index
        for i in range(len(nums) - 1, -1, -1):
            
            if abs(nums[left]) < abs(nums[right]):
                squared = nums[right] * nums[right]
                right = right -1
            else:
                squared = nums[left] * nums[left]
                left = left + 1
                
            sortedSquares[i] = squared
        
        return sortedSquares
 
            
            
            
            
            