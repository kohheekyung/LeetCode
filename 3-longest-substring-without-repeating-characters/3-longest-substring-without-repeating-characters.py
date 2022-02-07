class Solution(object): 
    
    
    '''Approach 1: Brute Force : Check all the substring one by one to see if it has no        duplicate character
    
    Algorithm
    Suppose we have a function boolean allUnique(String substing) which will return true if the characters in the substring are all unique, otherwise false. We can iterate through all the possible substrings of the given string s and call the function allUnique. If it turns out to be true, then we update our answer of the maximum legth of substring without duplicate characters.
    
  1. enumerate all the strings
  2. Check the substring and update the result
        Fuction
        - declare a direct access table (dict or set) to record the occurrence of each character
        
    Time Complexity : O(n^3) Nested for loops n^2 and check loop n
    Space Complexity :  O(m) size of table 128

    '''
    def lengthOfLongestSubstring_BruteForce(self, s):
        """
        :type s: str
        :rtype: int
        """
        def check(start, end):
            chars = [0]*128
            for i in range(start, end+1):
                char = s[i]
                chars[ord(char)] += 1
                if chars[ord(char)] > 1 :
                    return False
            return True
        
        n = len(s)
        max_length = 0
        
        for i in range(n):
            for j in range(i,n):
                if check(i,j):
                    max_length = max(max_length, j-i+1)
                
        return max_length
    
        '''Approach 2: Sliding
    
    Algorithm
    We need two pointers left(to contract the window)and right(to extend the window)
    First set left, right index 0
    if there is no duplicated, extend to right and record the index of charsn
    if it has duplicates, contract the window until there is no duplicates
        
    Time Complexity : O(2n) = O(n) the worst case : if every chars are same in string, we have to contract the left index  n time and extent the right index n time. 
    Space Complexity :  O(m)  the worst case : depends of the size of string

    '''
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        left = right = 0

        max_len = 0
        while right < len(s):
            ch = s[right]
            
            if ch in dic.keys() and dic[ch] >= left and dic[ch] < right :
                left = dic[ch] + 1
          
            max_len = max(max_len, right - left + 1)
            dic[ch] = right
            right += 1

        return max_len
            
        
        
        