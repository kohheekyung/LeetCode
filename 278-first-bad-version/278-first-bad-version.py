# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
'''
import numpy as np

class Solution:
    
    def firstBadVersionLinearScan(self, n: int) -> int:
        '''
        [Time Exceed] Brute Force
        
        time complexity O(n)
        space complexity O(1)
        '''
        for version in range(1, n+1) :
            if isBadVersion(version):
                return version
    
    def firstBadVersion(self, n: int) -> int:
        '''
        [Accepted] Binary Search
        
        time compexity O(log N) : The search space is halved each time.
        space complexity O(1)        
        '''
        
        left = 1
        right = n
        
        
        while left < right:
            
            version = left + (right - left) // 2
            
            if isBadVersion(version):
                right = version
            else:
                left = version + 1
                
        # The first bad version is when left = right
        return left
            
            
            
            
            
            
            
            
            
            
            
    
   
        
            
            
         